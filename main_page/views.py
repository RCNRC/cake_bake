from django.shortcuts import render, redirect
from django.db import transaction
from user_page.models import User, Cake, Order, RecievedRequest, SenderURL
from django.core.exceptions import ObjectDoesNotExist
from funcs import pay
from urllib.parse import urlparse


@transaction.atomic
def index(request):
    sender_url = request.META.get('HTTP_REFERER')
    if sender_url:
        sender, _ = SenderURL.objects.get_or_create(url=sender_url)
        RecievedRequest.objects.create(sender_url=sender)
    if not request.GET:  # если ничего не вводится на странице, то остаемся на ней
        return render(request, 'index.html')
    phonenumber = request.GET.get('REG', '')  # проверка введен ли номер в регистрации
    phone = ''
    for litera in phonenumber:
        try:
            int(litera)
            phone += litera
        except ValueError:
            continue
        url = request.build_absolute_uri()
        url = urlparse(url)
        url = ''.join((url.netloc, url.path))
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
        # cake.save()
        cake_id = cake.id
        Order.objects.create(
            cake=cake, user=user, address=address, date=date, time=time, comments=comments, delivcomments=delivcomments,
        )
        url = request.build_absolute_uri()
        url = urlparse(url)
        url = ''.join((url.scheme, '://', url.netloc, url.path))
        return pay(cake_id, url)
    try:  # если телефон в чердаке введен и клиент существует перенаправляем на страницу заказа
        User.objects.get(phonenumber=phonenumber)
        return redirect(f'lk-order/{phone}/')
    except ObjectDoesNotExist:  # если телефон в чердаке введен и клиент не существует перенаправляем на страницу лк
        # для дпльнейшей  регистрации
        return redirect('lk')
