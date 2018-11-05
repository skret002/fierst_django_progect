# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-30 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docprodukt',
            options={'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430 \u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b', 'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0430 \u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b'},
        ),
        migrations.RemoveField(
            model_name='optiondocfield',
            name='with_margin',
        ),
        migrations.AlterField(
            model_name='docprodukt',
            name='price_big_shipment',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u043e\u0442 20 \u0434\u043e 100\u0448\u0442'),
        ),
        migrations.AlterField(
            model_name='docprodukt',
            name='price_medium_shipment',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u043e\u0442 20 \u0434\u043e 100\u0448\u0442'),
        ),
        migrations.AlterField(
            model_name='docprodukt',
            name='price_smollshipment',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0434\u043e 20\u0448\u0442'),
        ),
    ]
