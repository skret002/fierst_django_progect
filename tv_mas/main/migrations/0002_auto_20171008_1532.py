# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_item',
            name='address',
            field=models.CharField(blank=True, max_length=60, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0432 \u0422\u041e\u041f\u0415'),
        ),
        migrations.AddField(
            model_name='top_item',
            name='telephone',
            field=models.CharField(blank=True, max_length=24, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b \u0432 \u0422\u041e\u041f\u0415'),
        ),
    ]