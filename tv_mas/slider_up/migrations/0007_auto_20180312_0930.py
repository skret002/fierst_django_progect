# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_up', '0006_auto_20171225_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider_image',
            name='image',
            field=models.ImageField(upload_to='products_images/', verbose_name='\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0434\u043b\u044f \u043f\u043a'),
        ),
    ]