# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0027_issuesprodukt_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuesprodukt',
            name='user',
        ),
    ]
