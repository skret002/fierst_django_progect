# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0074_auto_20180211_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.Status'),
        ),
    ]