# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-30 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bosstock',
            options={'verbose_name': '挂单', 'verbose_name_plural': '挂单'},
        ),
        migrations.AlterModelOptions(
            name='dealstock',
            options={'verbose_name': '交易记录', 'verbose_name_plural': '交易记录'},
        ),
        migrations.AlterField(
            model_name='bosstock',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='dealstock',
            name='dealtime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='交易时间'),
        ),
    ]