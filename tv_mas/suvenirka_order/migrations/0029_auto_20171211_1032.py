# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0028_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='userimages',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.Userimage'),
        ),
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
