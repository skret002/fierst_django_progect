# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-21 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0060_auto_20171221_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='us_image',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.Userimage'),
            preserve_default=False,
        ),
    ]
