from django.shortcuts import render, redirect
from django.db import transaction
from user_page.models import User, Cake


@transaction.atomic
def index(request):
    if not request.GET:  # если ничего не вводится на странице, то остаемся на ней
        return render(request, 'index.html')
    phonenumber = request.GET.get('REG', '')  # проверка введен ли номер в регистрации
    if not phonenumber:  # если нет то создаем нового клиента в базе из данных в заказе
        firstname = request.GET['NAME']
        phonenumber = request.GET['PHONE']
        email = request.GET['EMAIL']
        levels = request.GET['LEVELS']
        form = request.GET['FORM']
        topping = request.GET['TOPPING']
        berries = request.GET.get('BERRIES', None)
        decor = request.GET.get('DECOR', None)
        words = request.GET.get('WORDS', None)
        user = User.objects.create(firstname=firstname, phonenumber=phonenumber, email=email)
        Cake.objects.create(
            user=user, levels=levels, form=form, topping=topping, berries=berries, decor=decor, words=words,
        )
        return redirect('lk-order')
    try:  # если телефон в чердаке введен и клиент существует перенаправляем на страницу заказа
        user = User.objects.get(phonenumber=phonenumber)
        return redirect('lk-order')
    except User.DoesNotExist:  # если телефон в чердаке введен и клиент не существует перенаправляем на страницу лк для дпльнейшей  регистрации
        return redirect('lk')
