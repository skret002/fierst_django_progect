# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0017_productinbasket_color_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='color_check',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
