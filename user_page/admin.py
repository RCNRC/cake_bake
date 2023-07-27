from django.contrib import admin
from .models import User, Cake


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phonenumber']


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost']
