# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-03 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartridgesNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u041a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0430')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0430',
                'db_table': 'CartridgesNumber',
                'managed': True,
                'verbose_name_plural': '\u041d\u043e\u043c\u0435\u0440\u0430 \u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0435\u0439',
            },
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u0411\u0440\u0435\u043d\u0434')),
                ('model', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u041c\u043e\u0434\u0435\u043b\u044c \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u0430',
                'db_table': 'PrinterModel',
                'managed': True,
                'verbose_name_plural': '\u041c\u043e\u0434\u0435\u043b\u0438 \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, default=None, max_length=70, null=True, verbose_name='\u0423\u0441\u043b\u0443\u0433\u0430 \u0438\u043b\u0438 \u0442\u043e\u0432\u0430\u0440')),
                ('printe_or_cartridge', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='devaices', to='refcartridges.PrinterModel')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430 \u043a \u043c\u043e\u0434\u0435\u043b\u0438 \u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0430 \u0438\u043b\u0438 \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u0430',
                'db_table': 'Cartridges_Services',
                'managed': True,
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438 \u043a \u043c\u043e\u0434\u0435\u043b\u0438 \u043a\u0430\u0440\u0442\u0440\u0438\u0434\u0436\u0435\u0439 \u0438\u043b\u0438 \u043f\u0440\u0438\u043d\u0442\u0435\u0440\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='cartridgesnumber',
            name='printer',
            field=models.ForeignKey(blank=True, default=None, max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='printer_model', to='refcartridges.PrinterModel'),
        ),
    ]