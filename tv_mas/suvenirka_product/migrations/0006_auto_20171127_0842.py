# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0005_auto_20171127_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f -2'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f -3'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f -4'),
        ),
        migrations.AlterField(
            model_name='colorfield',
            name='color_img',
            field=models.ImageField(blank=True, default='\u0431\u0435\u043b\u044b\u0439', null=True, upload_to='products_images/', verbose_name='\u0446\u0432\u0435\u0442 \u0442\u043e\u0432\u0430\u0440\u0430 (\u0444\u043e\u0442\u043e)'),
        ),
    ]