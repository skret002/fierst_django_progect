# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 09:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_user_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_order',
        ),
    ]