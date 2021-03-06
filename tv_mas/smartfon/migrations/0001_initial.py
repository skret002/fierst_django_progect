# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-29 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(blank=True, default=None, max_length=100, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0431\u043b\u0435\u043c')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0431\u043b\u0435\u043c',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043f\u0440\u043e\u0431\u043b\u0435\u043c',
            },
        ),
        migrations.CreateModel(
            name='ChoicesAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.CharField(blank=True, default=None, max_length=50, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0417\u0427')),
            ],
            options={
                'verbose_name': '\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0417\u0427',
                'verbose_name_plural': '\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0417\u0427',
            },
        ),
        migrations.CreateModel(
            name='DopInfoService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_sc', models.TextField(max_length=1500, verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442 - \u0441\u0435\u0440\u0432\u0438\u0441 (\u0442\u0435\u043a\u0441\u0442)')),
                ('info_sc', models.TextField(max_length=1500, verbose_name='\u041a\u0442\u043e \u0440\u0435\u043c\u043e\u043d\u0442\u0438\u0440\u0443\u0435\u0442, \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430, \u043d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b (\u0442\u0435\u043a\u0441\u0442)')),
                ('info_prise', models.TextField(max_length=1500, verbose_name='\u041e \u0446\u0435\u043d\u0430\u0445 \u0438 \u0433\u0430\u0440\u0430\u043d\u0442\u0438\u0438 (\u0442\u0435\u043a\u0441\u0442)')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0442\u043e\u0432\u0430\u0440\u0430',
                'db_table': 'dop_info_service',
                'managed': True,
                'verbose_name_plural': '\u0422\u0435\u043a\u0441\u0442\u044b \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0442\u043e\u0432\u0430\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36, null=True, verbose_name=' \u0418\u043c\u044f ')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440')),
                ('order_option', models.CharField(choices=[('0', '\u041d\u0435 \u043d\u0443\u0436\u043d\u043e'), ('1', '\u0412\u044b\u0437\u0432\u0430\u0442\u044c \u043c\u0430\u0441\u0442\u0435\u0440\u0430'), ('2', '\u0412\u044b\u0437\u0432\u0430\u0442\u044c \u043a\u0443\u0440\u044c\u0435\u0440\u0430')], max_length=1, null=True, verbose_name='\u0417\u0430\u043a\u0430\u0437 \u0441 \u0432\u044b\u0435\u0437\u0434\u043e\u043c?')),
                ('order_day', models.CharField(blank=True, choices=[('0', '\u041f\u041d'), ('1', '\u0412\u0422'), ('2', '\u0421\u0420'), ('3', '\u0427\u0422'), ('4', '\u041f\u0422'), ('5', '\u0421\u0411'), ('6', '\u0412\u0421')], max_length=1, null=True, verbose_name='\u041d\u0430 \u043a\u0430\u043a\u043e\u0439 \u0434\u0435\u043d\u044c')),
                ('order_time', models.CharField(blank=True, choices=[('1', '8:00'), ('2', '8:30'), ('3', '9:00'), ('4', '9:30'), ('5', '10:00'), ('6', '10:30'), ('7', '11:00'), ('8', '11:30'), ('9', '12:00'), ('10', '12:30'), ('11', '13:00'), ('12', '13:30'), ('13', '14:00'), ('14', '14:30'), ('15', '15:00'), ('16', '15:30'), ('17', '16:00'), ('18', '16:30'), ('19', '17:00'), ('20', '17:30'), ('21', '18:00'), ('22', '18:30'), ('23', '19:00'), ('24', '19:30'), ('25', '20:00'), ('26', '20:30'), ('27', '21:00')], max_length=2, null=True, verbose_name='\u041d\u0430 \u043a\u0430\u043a\u043e\u0435 \u0432\u0440\u0435\u043c\u044f')),
                ('location', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('order_problem_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 ')),
                ('order_problem_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b: \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('read_unread', models.CharField(blank=True, choices=[('False', '\u041d\u0435 \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e'), ('True', '\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u043d\u043e')], default=False, max_length=10, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('final_status_order', models.CharField(blank=True, choices=[('0', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u043a\u0443\u0440\u044c\u0435\u0440'), ('1', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u043c\u0430\u0441\u0442\u0435\u0440'), ('2', '\u0417\u0430\u044f\u0432\u043a\u0430 \u043f\u0440\u043e\u0434\u0430\u043d\u0430 \u0434\u0440\u0443\u0433\u043e\u043c\u0443 \u0421\u0426')], max_length=2, null=True, verbose_name='\u0424\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430')),
                ('payment', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='\u0414\u043e\u0445\u043e\u0434 \u0441 \u0437\u0430\u044f\u0432\u043a\u0438')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0417\u0430\u044f\u0432\u043a\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0430')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u0417\u0430\u044f\u0432\u043a\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0430')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437 \u043d\u0430 \u0440\u0435\u043c\u043e\u043d\u0442 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u0430 & \u043f\u043b\u0430\u043d\u0448\u0435\u0442\u0430',
                'db_table': 'ref_smatfon_order',
                'managed': True,
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b \u043d\u0430 \u0440\u0435\u043c\u043e\u043d\u0442 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u043e\u0432 & \u043f\u043b\u0430\u043d\u0448\u0435\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='OutService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_out_service', models.CharField(blank=True, max_length=500, null=True, verbose_name='\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u0432\u044b\u0435\u0437\u0434\u0430')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u0432\u044b\u0435\u0437\u0434\u0430',
                'db_table': 'OutService',
                'managed': True,
                'verbose_name_plural': '\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u0432\u044b\u0435\u0437\u0434\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='PriceService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('part_price_zero', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='% \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u044b \u0417\u0427: \u0415\u0441\u043b\u0438 \u0434\u043e 100\u0440')),
                ('part_price_one', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='% \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u044b \u0417\u0427: \u0415\u0441\u043b\u0438 \u0434\u043e 350\u0440')),
                ('part_price_two', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='% \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u044b \u0417\u0427: \u0415\u0441\u043b\u0438 350-700\u0440')),
                ('part_price_three', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='% \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u044b \u0417\u0427: \u0415\u0441\u043b\u0438 700-2000\u0440')),
                ('part_price_four', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='% \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u044b \u0417\u0427: \u0415\u0441\u043b\u0438 2000-5000\u0440')),
                ('part_price_five', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='% \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435 \u0446\u0435\u043d\u044b \u0417\u0427: \u0415\u0441\u043b\u0438 > 5000\u0440')),
                ('price_one', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0420\u0430\u0431\u043e\u0442 - \u0415\u0441\u043b\u0438 \u0446\u0435\u043d\u0430 \u0417\u0427 \u0434\u043e 1500\u0440')),
                ('price_two', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0420\u0430\u0431\u043e\u0442 - \u0415\u0441\u043b\u0438 \u0446\u0435\u043d\u0430 \u0417\u0427 1500-3500\u0440')),
                ('price_three', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0420\u0430\u0431\u043e\u0442 - \u0415\u0441\u043b\u0438 \u0446\u0435\u043d\u0430 \u0417\u0427 3500\u0440-7000\u0440')),
                ('price_four', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0420\u0430\u0431\u043e\u0442 - \u0415\u0441\u043b\u0438 \u0446\u0435\u043d\u0430 \u0417\u0427 7000-10000\u0440')),
                ('price_five', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0420\u0430\u0431\u043e\u0442 - \u0415\u0441\u043b\u0438 \u0446\u0435\u043d\u0430 \u0417\u0427 > 10000\u0440')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0430\u0431\u043e\u0442 \u0438 \u043d\u0430\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u0417\u0427',
                'verbose_name_plural': '\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u0440\u0430\u0431\u043e\u0442 \u0438 \u043d\u0430\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u0417\u0427',
            },
        ),
        migrations.CreateModel(
            name='QualityPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(blank=True, default=None, max_length=100, verbose_name='\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0435\u0439')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0435\u0439',
                'verbose_name_plural': '\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0447\u0430\u0441\u0442\u0435\u0439',
            },
        ),
        migrations.CreateModel(
            name='RepairPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, default=None, max_length=24, verbose_name='\u0413\u0434\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u0435\u043d \u0440\u0435\u043c\u043e\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0413\u0434\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u0435\u043d \u0440\u0435\u043c\u043e\u043d\u0442',
                'verbose_name_plural': '\u0413\u0434\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b \u0440\u0435\u043c\u043e\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='SmartfonBrend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='\u0411\u0440\u0435\u043d\u0434')),
                ('image_brend', models.ImageField(blank=True, null=True, upload_to='smarfon_brend/', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u0431\u0440\u0435\u043d\u0434\u0430')),
                ('description_brend', models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0411\u0440\u0435\u043d\u0434\u0430')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0411\u0440\u0435\u043d\u0434 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u0430',
                'verbose_name_plural': '\u0411\u0440\u0435\u043d\u0434\u044b \u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='SmartfonModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c')),
                ('description_models', models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u0438')),
                ('image_models', models.ImageField(blank=True, null=True, upload_to='smarfon_model/', verbose_name='\u0424\u043e\u0442\u043e \u043c\u043e\u0434\u0435\u043b\u0438')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brend_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smartfon_brend', to='smartfon.SmartfonBrend')),
            ],
            options={
                'verbose_name': '\u041c\u043e\u0434\u0435\u043b\u044c \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u0430',
                'verbose_name_plural': '\u041c\u043e\u0434\u0435\u043b\u0438 \u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Spare_Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_service', models.CharField(blank=True, default=None, max_length=200, null=True, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0423\u0441\u043b\u0443\u0433\u0438')),
                ('popular_service', models.BooleanField(default=None, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0432 \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('autocheck', models.BooleanField(default=True, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0430\u0432\u0442\u043e\u043f\u0440\u043e\u0441\u0447\u0435\u0442 \u0446\u0435\u043d\u044b')),
                ('sale', models.BooleanField(default=False, verbose_name='\u0422\u043e\u0432\u0430\u0440 \u0432 \u0430\u043a\u0446\u0438\u0438')),
                ('price_sale', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430 \u043f\u043e \u0430\u043a\u0446\u0438\u0438 \u0432 \u0440\u0443\u0431.')),
                ('all_smartfon', models.BooleanField(default=False, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0443 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043c\u043e\u0434\u0435\u043b\u0435\u0439')),
                ('base_prise', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u0420\u0435\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430 \u0417\u0427')),
                ('full_prise', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u0430')),
                ('time_on_repairs', models.CharField(blank=True, default=None, max_length=60, null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u0440\u0435\u043c\u043e\u043d\u0442')),
                ('description_service', models.TextField(blank=True, default=None, max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0423\u0441\u043b\u0443\u0433\u0438')),
                ('image_part_base', models.ImageField(blank=True, null=True, upload_to='smarfon_part/', verbose_name='\u0424\u043e\u0442\u043e \u0417\u0430\u043f\u0447\u0430\u0441\u0442\u0438')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('action_problem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smartfon.ActionProblem', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0431\u043b\u0435\u043c')),
                ('available_part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices_available', to='smartfon.ChoicesAvailable', verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0417\u0427')),
                ('quality_part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quality_part', to='smartfon.QualityPart', verbose_name='\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0417\u0427')),
                ('repair_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repair_place', to='smartfon.RepairPlace', verbose_name='\u0413\u0434\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u0435\u043d \u0440\u0435\u043c\u043e\u043d\u0442')),
                ('smartfonmodels', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='smarfon_models', to='smartfon.SmartfonModels')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043f\u0447\u0430\u0442\u044c  \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u0430',
                'verbose_name_plural': '\u0417\u0430\u043f\u0447\u0430\u0441\u0442\u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u043e\u0432',
            },
        ),
    ]
