# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-13 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductInfo', '0004_auto_20180613_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='ProductNumber',
            field=models.CharField(max_length=30, verbose_name='规格'),
        ),
    ]