# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tv', '0009_auto_20180427_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv_repair',
            name='number_tv_model',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tv_repair', to='repair_tv.Tv_Models'),
        ),
    ]