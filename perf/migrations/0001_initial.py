# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-23 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('perf_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u5e8f\u53f7')),
                ('name', models.CharField(max_length=8, verbose_name='\u59d3\u540d')),
                ('team', models.CharField(choices=[('\u4e00\u5ba4', '\u4e00\u5ba4'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4'), ('\u4e09\u5ba4', '\u4e09\u5ba4'), ('\u56e2\u961f', '\u56e2\u961f')], max_length=4, verbose_name='\u5ba4\u522b')),
                ('performance', models.FloatField(choices=[(5.0, '\u6311\u884c\u674e   \u4ef6/1\u6b21'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.0, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (10.0, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (20.0, '\u8d85\u5927/\u5c0f\u65f6'), (20.0, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.0, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.0, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.0, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff09\uff08\u8bf7\u5907\u6ce8\uff09'), (1.0, '\u5176\u4ed6   /\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], max_length=4, verbose_name='\u9879\u76ee')),
                ('values', models.FloatField(max_length=4, verbose_name='\u6570\u503c')),
                ('workload', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
                ('verify', models.CharField(choices=[('\u7b49\u5f85\u5ba1\u6838', '\u7b49\u5f85\u5ba1\u6838'), ('\u672a\u901a\u8fc7\u5ba1\u6838', '\u672a\u901a\u8fc7\u5ba1\u6838'), ('\u5df2\u5ba1\u6838', '\u5df2\u5ba1\u6838')], default='\u7b49\u5f85\u5ba1\u6838', max_length=10, verbose_name='\u5ba1\u6838\u72b6\u6001')),
                ('verify_auth', models.CharField(max_length=8, verbose_name='\u5ba1\u6838\u4eba')),
                ('verify_date', models.DateTimeField(verbose_name='\u5ba1\u6838\u65f6\u95f4')),
                ('comment', models.TextField(default='\u65e0', max_length=40, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u7ee9\u6548',
                'verbose_name_plural': '\u7ee9\u6548\u767b\u8bb0',
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='\u59d3\u540d')),
                ('team', models.CharField(choices=[('\u4e00\u5ba4', '\u4e00\u5ba4'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4'), ('\u4e09\u5ba4', '\u4e09\u5ba4'), ('\u56e2\u961f', '\u56e2\u961f')], max_length=4, verbose_name='\u5ba4\u522b')),
                ('year', models.IntegerField(choices=[(2016, '2016')], verbose_name='\u5e74\u4efd')),
                ('month', models.IntegerField(choices=[(1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12')], verbose_name='\u6708\u4efd')),
                ('workload', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
            ],
            options={
                'verbose_name': '\u7ee9\u6548\u7edf\u8ba1',
                'verbose_name_plural': '\u7ee9\u6548\u7edf\u8ba1',
            },
        ),
    ]