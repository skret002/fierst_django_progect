# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-30 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_documents', '0002_auto_20181030_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docprodukt',
            name='format_photo',
            field=models.CharField(blank=True, default=None, max_length=15, verbose_name='\u0422\u0438\u043f \u0423\u0441\u043b\u0443\u0433\u0438'),
        ),
    ]