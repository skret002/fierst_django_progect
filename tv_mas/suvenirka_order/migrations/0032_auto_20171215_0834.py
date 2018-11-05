# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0031_remove_order_userimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userimage',
            options={'verbose_name': '\u0444\u043e\u0442\u043e \u043a \u0437\u0430\u043a\u0430\u0437\u0443', 'verbose_name_plural': '\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u043a \u0437\u0430\u043a\u0430\u0437\u0443'},
        ),
        migrations.AddField(
            model_name='userimage',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
