from django.shortcuts import render, redirect
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from user_page.models import User


@transaction.atomic
def index(request):
    if not request.GET:
        return render(request, 'index.html')
    phonenumber = request.GET.get('REG', '')
    if not phonenumber:
        firstname = request.GET['NAME']
        phonenumber = request.GET['PHONE']
        email = request.GET['EMAIL']
        User.objects.create(firstname=firstname, phonenumber=phonenumber, email=email)
        return redirect('lk-order')
    try:
        user = User.objects.get(phonenumber=phonenumber)
        return render(request, 'index.html')
    except User.DoesNotExist:
        return redirect('lk')




