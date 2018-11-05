# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-20 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20180918_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.DocumentCount', verbose_name='\u043a\u043e\u0434-\u0432\u043e \u0444\u043e\u0442\u043e \u0432 \u0431\u043b\u043e\u043a\u0435')),
                ('edit_price_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.DocumentEditPrice', verbose_name='\u0446\u0435\u043d\u0430 \u0442\u043e\u043b\u044c\u043a\u043e \u0437\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443')),
                ('full_price_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.DocumentFullPrice', verbose_name='\u043f\u043e\u043b\u043d\u0430\u044f \u0446\u0435\u043d\u0430 \u0441 \u043f\u0435\u0447\u0430\u0442\u044c\u044e')),
                ('image_preview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.DocumentImagePreview', verbose_name='\u043f\u0440\u0438\u043c\u0435\u0440 \u0431\u043b\u043e\u043a\u0430')),
                ('options_photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.DocumentOptions', verbose_name='\u043e\u043f\u0446\u0438\u0438 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439')),
            ],
        ),
        migrations.AlterField(
            model_name='header',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0432 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0435'),
        ),
    ]
