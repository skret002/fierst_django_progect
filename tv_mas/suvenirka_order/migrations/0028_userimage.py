# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-11 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0027_auto_20171210_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='user_image/')),
            ],
        ),
    ]