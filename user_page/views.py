from django.shortcuts import render, redirect
from .models import User


def private_area(request):
    # TODO нужно ещё разобраться: 1) будет ли пользователь в запросе или его по токену искать лучше, 2) нужно ли мне уже сразу шаблонизировать страницу
    return render(request, 'lk.html')


def private_area_order(request, phonenumber=None):
    try:
        if phonenumber and phonenumber[0] == '8':
            phonenumber = '+7' + phonenumber[1:]
        user = User.objects.get(phonenumber=phonenumber)
        context = {
            'user': user,
            'orders': user.orders.all(),
        }
        return render(request, 'lk-order.html', context=context)
    except User.DoesNotExist:
        return redirect('main')
