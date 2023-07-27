# Generated by Django 4.2.3 on 2023-07-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0006_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivecomments',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(null=True, verbose_name='дата доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivcomments',
            field=models.TextField(blank=True, verbose_name='комментарии к доставке'),
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(null=True, verbose_name='время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.TextField(blank=True, verbose_name='комментарии к заказу'),
        ),
    ]