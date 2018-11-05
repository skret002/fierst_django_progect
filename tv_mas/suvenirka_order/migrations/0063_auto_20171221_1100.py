# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-21 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0062_auto_20171221_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='us_image',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='us_image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.Userimage'),
            preserve_default=False,
        ),
    ]
