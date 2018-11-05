# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0035_productinorder_user_photo_in_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinorder',
            name='user_photo_in_order',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='image',
            field=models.FileField(default=1, upload_to='user_image/'),
            preserve_default=False,
        ),
    ]