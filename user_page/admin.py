from django.contrib import admin
from .models import User, Cake, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'phonenumber']


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['words', 'cost']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost']
