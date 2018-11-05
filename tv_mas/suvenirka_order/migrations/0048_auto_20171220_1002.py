# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0047_auto_20171220_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='us_image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.Userimage'),
            preserve_default=False,
        ),
    ]