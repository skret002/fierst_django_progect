# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0011_auto_20171203_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='prod_color_color_img',
        ),
        migrations.RemoveField(
            model_name='productinbasket',
            name='prod_color_name',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='prod_color_name',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
