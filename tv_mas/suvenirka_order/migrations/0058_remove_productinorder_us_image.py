# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0057_order_us_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinorder',
            name='us_image',
        ),
    ]