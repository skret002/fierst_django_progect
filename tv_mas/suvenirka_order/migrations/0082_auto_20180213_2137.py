# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suvenirka_product', '0026_auto_20180116_0758'),
        ('suvenirka_order', '0081_productinbasket_issues_produkt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='issues_produkt',
        ),
        migrations.AddField(
            model_name='productinorder',
            name='issues_produkt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='suvenirka_product.IssuesProdukt'),
        ),
    ]
