# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0002_auto_20171117_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_img', models.ImageField(upload_to='products_images/', verbose_name='\u0446\u0432\u0435\u0442 \u0442\u043e\u0432\u0430\u0440\u0430 (\u0444\u043e\u0442\u043e)')),
            ],
            options={
                'verbose_name': '\u0446\u0432\u0435\u0442 \u0442\u043e\u0432\u0430\u0440\u0430(img)',
                'verbose_name_plural': '\u0446\u0432\u0435\u0442 \u0442\u043e\u0432\u0430\u0440\u043e\u0432(img)',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=None, upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f -2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=None, upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f -3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default=1, upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f -4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='\u0440\u0430\u0437\u043c\u0435\u0440'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products_images/', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_primer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_product.ColorField'),
            preserve_default=False,
        ),
    ]
