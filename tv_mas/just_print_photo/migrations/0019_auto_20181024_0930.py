# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-24 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_print_photo', '0018_auto_20181023_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count_price',
            field=models.DecimalField(decimal_places=0, max_digits=9, verbose_name='\u0412\u0441\u0435\u0433\u043e \u043a \u043e\u043f\u043b\u0430\u0442\u0435'),
        ),
    ]
