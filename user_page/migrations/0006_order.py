# Generated by Django 4.2.3 on 2023-07-27 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0005_cake_words'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(verbose_name='комментарии к заказу')),
                ('delivecomments', models.TextField(verbose_name='комментарии к доставке')),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='user_page.cake', verbose_name='торт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='user_page.user', verbose_name='заказчик')),
            ],
        ),
    ]
