from django.contrib import admin
from .models import User, Cake, Order, SenderURL, RecievedRequest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'phonenumber']


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['words', 'cost']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost']


class RecievedRequestInline(admin.TabularInline):
    extra = 0
    model = RecievedRequest


@admin.register(SenderURL)
class SenderURLAdmin(admin.ModelAdmin):
    fields = ['url']
    list_display = ['url']
    inlines = [
        RecievedRequestInline,
    ]
