# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-27 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import repair_tv.models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tv', '0007_auto_20180427_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv_repair',
            name='number_tv_model',
            field=models.BooleanField(default=1, verbose_name=repair_tv.models.Tv_Models),
            preserve_default=False,
        ),
    ]
