# Generated by Django 3.2 on 2022-10-03 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name=' Товар')),
                ('product_description', models.TextField(max_length=3000, verbose_name='Описание товара')),
                ('product_image', models.TextField(max_length=3000, verbose_name='Изображение')),
                ('product_category', models.CharField(choices=[('other', 'Разное'), ('televisions', 'Телевизоры'), ('refrigerators', 'Холодильники'), ('electric_kettles', 'Электрочайники')], default='other', max_length=100, verbose_name=' Товар')),
                ('state', models.CharField(choices=[('ACTIVE', 'Active'), ('NOT_ACTIVE', 'Not Active')], default='ACTIVE', max_length=100, verbose_name='Состояние')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, max_length=100, verbose_name='Стоимость')),
                ('remains', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток')),
            ],
        ),
    ]
