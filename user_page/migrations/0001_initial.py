# Generated by Django 4.2.3 on 2023-07-26 01:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('firstname', models.CharField(max_length=75, verbose_name='имя')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, primary_key=True, region=None, serialize=False, verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
            ],
        ),
    ]
