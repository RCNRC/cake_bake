from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cake_bake import settings
from cake_bake.settings import COST


class User(models.Model):
    firstname = models.CharField(
        verbose_name='имя',
        max_length=75,
    )
    phonenumber = PhoneNumberField(
        verbose_name='номер телефона',
        primary_key=True,
    )
    email = models.EmailField(
        verbose_name='почта',
        max_length=254,
    )

    def __str__(self):
        return self.firstname


class Cake(models.Model):
    levels = models.PositiveSmallIntegerField(verbose_name='количество уровней', choices=settings.LEVELS, default=1)
    form = models.PositiveSmallIntegerField(verbose_name='форма', choices=settings.FORMS, default=1)
    topping = models.PositiveSmallIntegerField(verbose_name='топпинг', choices=settings.TOPPINGS, default=1)
    berries = models.PositiveSmallIntegerField(verbose_name='ягоды', choices=settings.BERRIES, default=None, null=True,
                                               blank=True)
    decor = models.PositiveSmallIntegerField(verbose_name='декор', choices=settings.DECORS, default=None, null=True,
                                             blank=True)
    words = models.CharField(verbose_name='надпись', max_length=50, default=None, null=True, blank=True)

    def cost(self):
        cost = sum((COST['levels'][self.levels], COST['form'][self.form], COST['topping'][self.topping],
                    COST['berries'].get(self.berries, 0), COST['decor'].get(self.decor, 0)))
        if self.words:
            cost += 500
        return cost

    def __str__(self):
        return f'{self.words}, цена: {self.cost()}'


class Order(models.Model):
    WAIT_MANAGER = 'WM'
    WAIT_RESTAURANT = 'WR'
    WAIT_COURIER = 'WC'
    CLOSED = 'CL'
    STATUSES = [
        (WAIT_MANAGER, 'Необработанный'),
        (WAIT_RESTAURANT, 'Ожидание рестарана'),
        (WAIT_COURIER, 'Ожидание курьера'),
        (CLOSED, 'Завершён'),
    ]

    cake = models.ForeignKey(
        Cake, verbose_name='торт', related_name='orders', on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        verbose_name='заказчик',
        related_name='orders',
        on_delete=models.CASCADE,
        null=True,
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=2,
        choices=STATUSES,
        default=WAIT_MANAGER,
        db_index=True,
    )

    address = models.CharField(verbose_name='адрес', max_length=300)
    date = models.DateField(verbose_name='дата доставки')
    time = models.TimeField(verbose_name='время доставки')
    comments = models.TextField(verbose_name='комментарии к заказу', blank=True)
    delivcomments = models.TextField(verbose_name='комментарии к доставке', blank=True)

    def cost(self):
        return self.cake.cost()


class SenderURL(models.Model):
    url = models.TextField(
        verbose_name='url',
        db_index=True,
        unique=True,
    )

    def count(self):
        return self.requests.length()


class RecievedRequest(models.Model):
    sender_url = models.ForeignKey(
        SenderURL,
        on_delete=models.CASCADE,
        verbose_name='url отправителя',
        related_name='requests',
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата запроса',
    )
