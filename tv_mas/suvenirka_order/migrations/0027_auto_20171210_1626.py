# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_order', '0026_auto_20171210_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(upload_to='pic_folder/')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='userimages',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.ExampleModel'),
        ),
    ]
