# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0010_auto_20171129_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='prod_color_color_img',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='prod_color_name',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
