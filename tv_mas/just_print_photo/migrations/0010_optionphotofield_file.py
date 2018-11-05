# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-22 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('just_print_photo', '0009_auto_20181022_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionphotofield',
            name='file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='file_user_photo', to='just_print_photo.FilePhoto', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438'),
            preserve_default=False,
        ),
    ]
