# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0031_auto_20180307_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description_category',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
