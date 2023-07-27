# Generated by Django 4.2.3 on 2023-07-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0002_cake'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='form',
            field=models.CharField(choices=[('circle', 'круг'), ('square', 'квадрат'), ('rectangle', 'прямоунольник')], default='circle', max_length=50, verbose_name='форма'),
        ),
        migrations.AddField(
            model_name='cake',
            name='topping',
            field=models.CharField(choices=[('none', 'без'), ('white', 'белый'), ('caramel', 'карамельный'), ('maple', 'кленовый'), ('bilberry', 'черничный'), ('milk_choco', 'молочный шоколад'), ('strawberry', 'клубничный')], default='none', max_length=50, verbose_name='топпинг'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='levels',
            field=models.PositiveSmallIntegerField(choices=[(1, 'один'), (2, 'два'), (3, 'три')], default=1, verbose_name='количество уровней'),
        ),
    ]
