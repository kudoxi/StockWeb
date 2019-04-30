# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-30 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20190430_0141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name': '银行', 'verbose_name_plural': '银行'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '发帖', 'verbose_name_plural': '发帖'},
        ),
        migrations.AlterModelOptions(
            name='blogtype',
            options={'verbose_name': '发帖类型', 'verbose_name_plural': '发帖类型'},
        ),
        migrations.AlterModelOptions(
            name='fund',
            options={'verbose_name': '钱包', 'verbose_name_plural': '钱包'},
        ),
        migrations.AlterModelOptions(
            name='selfstock',
            options={'verbose_name': '自选股', 'verbose_name_plural': '自选股'},
        ),
        migrations.AddField(
            model_name='bank',
            name='bankNo',
            field=models.CharField(max_length=64, null=True, verbose_name='银行卡号'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank',
            field=models.IntegerField(choices=[(0, '中国银行'), (1, '中国工商银行'), (2, '中国建设银行')], null=True, verbose_name='银行'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='password',
            field=models.CharField(max_length=255, null=True, verbose_name='支付密码'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='turename',
            field=models.CharField(max_length=64, null=True, verbose_name='真实姓名'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发帖日期'),
        ),
    ]
