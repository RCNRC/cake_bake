# Generated by Django 4.2.3 on 2023-07-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0004_cake_berries_cake_decor_alter_cake_form_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='words',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='надпись'),
        ),
    ]
