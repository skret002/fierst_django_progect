# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv_models',
            name='brend_logo',
            field=models.ImageField(default=1, upload_to='tv_model_images/', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u0431\u0440\u0435\u043d\u0434\u0430'),
            preserve_default=False,
        ),
    ]