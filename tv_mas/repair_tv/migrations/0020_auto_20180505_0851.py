# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-05 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('repair_tv', '0019_auto_20180502_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv_models',
            name='kgn',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, '\u041d\u0435 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u0422\u0412'), (2, '\u0414\u043b\u044f \u0432\u0441\u0435\u0445 \u0422\u0412')], max_length=3, null=True, verbose_name='\u041a\u043e\u0434 \u0443\u0441\u043b\u0443\u0433\u0438'),
        ),
        migrations.AddField(
            model_name='tv_repair',
            name='kgn',
            field=models.CharField(default=1, max_length=5, verbose_name=' \u041a\u043e\u0434 \u0413\u0440\u0443\u043f\u043f\u044b \u041d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u0438'),
        ),
    ]