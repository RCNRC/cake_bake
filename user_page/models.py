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
    user = models.ForeignKey(
        User, verbose_name='заказчик', related_name='cakes', on_delete=models.CASCADE,
    )
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
