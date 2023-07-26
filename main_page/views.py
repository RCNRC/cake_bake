from django.shortcuts import render
from django.db import transaction


@transaction.atomic
def index(request):
    # Если еть что в параметрах запроса то сохранить, иначе просто рендер
    return render(request, 'index.html')
