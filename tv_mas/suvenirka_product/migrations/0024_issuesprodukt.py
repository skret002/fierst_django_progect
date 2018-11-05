# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-25 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0023_auto_20171130_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuesProdukt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('you_name', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='\u0418\u043c\u044f')),
                ('you_phone', models.CharField(blank=True, default=None, max_length=18, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('you_question', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443 \u0432 \u0441\u0443\u0432\u0435\u043d\u0438\u0440\u043a\u0438',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443 \u0432 \u0441\u0443\u0432\u0435\u043d\u0438\u0440\u043a\u0438',
            },
        ),
    ]