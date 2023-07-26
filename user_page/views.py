from django.shortcuts import render


def private_area(request):
    # TODO нужно ещё разобраться: 1) будет ли пользователь в запросе или его по токену искать лучше, 2) нужно ли мне уже сразу шаблонизировать страницу
    return render(request, 'lk.html')


def private_area_order(request):
    # TODO аналогично
    return render(request, 'lk-order.html')
