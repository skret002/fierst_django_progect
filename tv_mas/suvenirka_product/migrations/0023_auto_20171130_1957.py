# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 19:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0022_auto_20171130_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colorfield',
            old_name='product',
            new_name='product_color',
        ),
    ]
