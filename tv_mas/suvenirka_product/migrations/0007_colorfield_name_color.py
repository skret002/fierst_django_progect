# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0006_auto_20171127_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorfield',
            name='name_color',
            field=models.CharField(blank=True, default='\u0431\u0435\u043b\u044b\u0439', max_length=16, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0446\u0432\u0435\u0442\u0430'),
        ),
    ]
