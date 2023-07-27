from django.shortcuts import render, redirect
from django.db import transaction
from user_page.models import User, Cake, Order
from django.core.exceptions import ObjectDoesNotExist


@transaction.atomic
def index(request):
    if not request.GET:  # если ничего не вводится на странице, то остаемся на ней
        return render(request, 'index.html')
    phonenumber = request.GET.get('REG', '')  # проверка введен ли номер в регистрации
    phone = ''
    for litera in phonenumber:
        try:
            int(litera)
            phone+=litera
        except ValueError:
            continue
    if not phone:  # если нет то создаем нового клиента в базе из данных в заказе
        firstname = request.GET['NAME']
        phonenumber = request.GET['PHONE']
        phone = ''
        for litera in phonenumber:
            try:
                int(litera)
                phone += litera
            except ValueError:
                continue
        print(type(phonenumber))
        email = request.GET['EMAIL']
        levels = request.GET['LEVELS']
        form = request.GET['FORM']
        topping = request.GET['TOPPING']
        berries = request.GET.get('BERRIES', None)
        decor = request.GET.get('DECOR', None)
        words = request.GET.get('WORDS', None)
        address = request.GET['ADDRESS']
        date = request.GET['DATE']
        time = request.GET['TIME']
        comments = request.GET['COMMENTS']
        delivcomments = request.GET['DELIVCOMMENTS']
        print(phonenumber)
        user, _ = User.objects.get_or_create(phonenumber=phonenumber)
        if not user:
            print('\nAAA\n')
            return render(request, 'index.html')
        user.firstname = firstname
        user.email = email
        user.save()
        cake = Cake.objects.create(
            levels=levels, form=form, topping=topping, berries=berries, decor=decor, words=words,
        )
        Order.objects.create(
            cake=cake, user=user, address=address, date=date, time=time, comments=comments, delivcomments=delivcomments,
        )
        return redirect(f'lk-order/{phonenumber}/')
    try:  # если телефон в чердаке введен и клиент существует перенаправляем на страницу заказа
        User.objects.get(phonenumber=phonenumber)
        return redirect(f'lk-order/{phonenumber}/')
    except ObjectDoesNotExist:  # если телефон в чердаке введен и клиент не существует перенаправляем на страницу лк для дпльнейшей  регистрации
        return redirect('lk')
