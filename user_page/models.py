from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
