# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-23 06:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180122_0841'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, default=b''),
        ),
    ]