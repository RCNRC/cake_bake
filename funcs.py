from django.shortcuts import redirect
from yookassa import Configuration, Payment
from cake_bake import settings
from user_page.models import Cake
import uuid
import json


def pay(cake_id, url):
    Configuration.account_id = settings.YK_ID
    Configuration.secret_key = settings.YK_SK
    cake = Cake.objects.get(id=cake_id)
    amount = cake.cost()
    payment = Payment.create({
        "amount": {
            "value": f"{amount}",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": url
        },
        "capture": True,
        "description": "description"
    }, uuid.uuid4())
    payment_details = json.loads(payment.json())
    url = payment_details['confirmation']['confirmation_url']
    return redirect(url)
