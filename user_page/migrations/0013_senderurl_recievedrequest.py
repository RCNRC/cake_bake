# Generated by Django 4.2.3 on 2023-07-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0012_remove_cake_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SenderURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(db_index=True, unique=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='RecievedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата запроса')),
                ('sender_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='user_page.senderurl', verbose_name='url отправителя')),
            ],
        ),
    ]
