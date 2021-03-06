# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suvenirka_order', '0083_remove_productinorder_issues_produkt'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSendingFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_order.Order')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0439 \u0438\u043c\u0435\u0439\u043b',
                'verbose_name_plural': '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u0438\u043c\u0435\u0439\u043b\u044b',
            },
        ),
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0418\u043c\u0435\u0439\u043b\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0418\u043c\u0435\u0439\u043b\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='emailsendingfact',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.EmailType'),
        ),
    ]
