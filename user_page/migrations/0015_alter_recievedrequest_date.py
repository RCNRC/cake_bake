# Generated by Django 4.2.3 on 2023-07-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0014_alter_recievedrequest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recievedrequest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата запроса'),
        ),
    ]