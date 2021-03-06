# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-13 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCar', '0002_auto_20180612_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mycars',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单'},
        ),
        migrations.AddField(
            model_name='mycars',
            name='table_num',
            field=models.IntegerField(default=0, verbose_name='桌号'),
        ),
        migrations.AlterField(
            model_name='mycars',
            name='ProductID',
            field=models.CharField(max_length=18, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='mycars',
            name='ProductName',
            field=models.CharField(max_length=30, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='mycars',
            name='ProductPrice',
            field=models.PositiveIntegerField(verbose_name='价格'),
        ),
    ]
