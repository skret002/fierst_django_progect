# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 18:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider_up', '0011_auto_20180312_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nameimage',
            name='f',
        ),
        migrations.DeleteModel(
            name='NameImage',
        ),
    ]