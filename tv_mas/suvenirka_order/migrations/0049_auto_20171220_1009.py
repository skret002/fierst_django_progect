# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-20 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0048_auto_20171220_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.FileField(blank=True, upload_to='..user_image/'),
        ),
    ]
