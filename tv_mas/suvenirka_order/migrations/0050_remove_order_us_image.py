# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 10:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0049_auto_20171220_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='us_image',
        ),
    ]
