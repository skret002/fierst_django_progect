# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-22 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('just_print_photo', '0014_auto_20181022_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionphotofield',
            name='comment',
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430'),
        ),
    ]