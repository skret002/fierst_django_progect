# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-26 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0009_auto_20180923_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderphoto',
            name='count_complect',
        ),
        migrations.RemoveField(
            model_name='orderphoto',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='orderphoto',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orderphoto',
            name='time',
        ),
        migrations.AddField(
            model_name='orderphoto',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='orderphoto',
            name='name_document',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='orderphoto',
            name='name_user',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='\u0418\u043c\u044f \u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430'),
        ),
        migrations.AddField(
            model_name='orderphoto',
            name='task',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', '\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0438 \u0432\u044b\u0441\u043b\u0430\u0442\u044c \u043d\u0430 \u043f\u043e\u0447\u0442\u0443'), ('2', '\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0431\u043b\u043e\u043a \u0444\u043e\u0442\u043e'), ('3', '\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0438 \u0432\u044b\u0441\u043b\u0430\u0442\u044c \u043d\u0430 \u043f\u043e\u0447\u0442\u0443')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
