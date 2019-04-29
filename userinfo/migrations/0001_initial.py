# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-29 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turename', models.CharField(max_length=64, verbose_name='真实姓名')),
                ('bank', models.IntegerField(choices=[(0, '中国银行'), (1, '中国工商银行'), (2, '中国建设银行')], verbose_name='银行')),
                ('password', models.CharField(max_length=255, verbose_name='支付密码')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('details', models.TextField(verbose_name='内容')),
                ('datetime', models.DateTimeField(verbose_name='发帖日期')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='博客类型')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='资金')),
                ('frozen_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='冻结资金')),
            ],
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='持有数量')),
                ('frozen_amount', models.IntegerField(verbose_name='冻结数量')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock', verbose_name='持有股票')),
            ],
        ),
        migrations.CreateModel(
            name='SelfStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock', verbose_name='股票')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('uphone', models.CharField(max_length=32, verbose_name='手机')),
                ('uemail', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否激活')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.AddField(
            model_name='selfstock',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='hold',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='持有用户'),
        ),
        migrations.AddField(
            model_name='fund',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.BlogType', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='发帖人'),
        ),
        migrations.AddField(
            model_name='bank',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo', verbose_name='用户'),
        ),
    ]
