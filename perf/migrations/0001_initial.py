# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 14:05
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
                ('performance', models.FloatField(choices=[(0.0, '\u65e0'), (5.0, '\u6311\u884c\u674e\u4ef6\u6570/\u6bcf\u6b21'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.1, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (10.1, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (20.2, '\u8d85\u5927/\u5c0f\u65f6'), (20.3, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.4, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.1, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.2, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff09\uff08\u8bf7\u5907\u6ce8\uff09'), (1.3, '\u5176\u4ed6   /\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], default=0.0, max_length=4, verbose_name='\u4efb\u52a11')),
                ('values', models.FloatField(default=0, max_length=4, verbose_name='\u6570\u503c1')),
                ('performancetwo', models.FloatField(choices=[(0.0, '\u65e0'), (5.0, '\u6311\u884c\u674e\u4ef6\u6570/\u6bcf\u6b21'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.1, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (10.1, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (20.2, '\u8d85\u5927/\u5c0f\u65f6'), (20.3, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.4, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.1, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.2, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff09\uff08\u8bf7\u5907\u6ce8\uff09'), (1.3, '\u5176\u4ed6   /\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], default=0.0, max_length=4, verbose_name='\u4efb\u52a12')),
                ('valuestwo', models.FloatField(default=0, max_length=4, verbose_name='\u6570\u503c2')),
                ('performancethree', models.FloatField(choices=[(0.0, '\u65e0'), (5.0, '\u6311\u884c\u674e\u4ef6\u6570/\u6bcf\u6b21'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.1, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (10.1, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u8bf7\u5907\u6ce8\u822a\u73ed\uff09'), (20.2, '\u8d85\u5927/\u5c0f\u65f6'), (20.3, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.4, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.1, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.2, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff09\uff08\u8bf7\u5907\u6ce8\uff09'), (1.3, '\u5176\u4ed6   /\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], default=0.0, max_length=4, verbose_name='\u4efb\u52a13')),
                ('valuesthree', models.FloatField(default=0, max_length=4, verbose_name='\u6570\u503c3')),
                ('workload', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
                ('supervisor', models.CharField(choices=[('\u4e00\u5ba4', '\u4e00\u5ba4\uff08\u7f57\u5fd7\u748b\u3001\u6bdb\u601d\u5b34\u3001\u8d75\u81e3\u7b49\uff09'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4\uff08\u59da\u79cb\u7115\u3001\u5218\u5468\u654f\u3001\u718a\u8f89\u3001\u6768\u4ef2\u8d24\u7b49\uff09'), ('\u4e09\u5ba4', '\u4e09\u5ba4\uff08\u5362\u4e98\u3001\u6e29\u5fd7\u68ee\u3001\u5434\u5a55\u73b2\u3001\u5218\u5072\u7fc0\u3001\u738b\u4f73\u3001\u9ec4\u6c5d\u535a\u7b49\uff09'), ('\u56e2\u961f', '\u56e2\u961f\uff08\u5434\u73b2\u3001\u6881\u826f\u7b49\uff09')], max_length=4, verbose_name='\u6307\u6d3e\u5ba4')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
                ('verify', models.CharField(choices=[('\u7b49\u5f85\u5ba1\u6838', '\u7b49\u5f85\u5ba1\u6838'), ('\u672a\u901a\u8fc7', '\u672a\u901a\u8fc7'), ('\u5df2\u5ba1\u6838', '\u5df2\u5ba1\u6838')], default='\u7b49\u5f85\u5ba1\u6838', max_length=10, verbose_name='\u5ba1\u6838\u72b6\u6001')),
                ('verify_auth', models.CharField(default='NULL', max_length=8, verbose_name='\u5ba1\u6838\u4eba')),
                ('verify_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u63d0\u4ea4/\u5ba1\u6838\u65f6\u95f4')),
                ('comment', models.TextField(default='\u65e0', max_length=40, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u7ee9\u6548',
                'verbose_name_plural': '\u7ee9\u6548\u767b\u8bb0',
            },
        ),
        migrations.CreateModel(
            name='Addother',
            fields=[
                ('other_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u5e8f\u53f7')),
                ('other_name', models.CharField(max_length=8, verbose_name='\u59d3\u540d')),
                ('other_team', models.CharField(choices=[('\u4e00\u5ba4', '\u4e00\u5ba4'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4'), ('\u4e09\u5ba4', '\u4e09\u5ba4'), ('\u56e2\u961f', '\u56e2\u961f')], max_length=4, verbose_name='\u5ba4\u522b')),
                ('airline', models.FloatField(choices=[(252.001, 'AF'), (72.006, 'BR'), (72.007, 'CI'), (72.002, 'JL'), (84.002, 'KA'), (72.004, 'KE'), (72.001, 'MH'), (72.005, 'OZ'), (108.001, 'OZ370+306'), (115.201, 'OZ356+306'), (100.801, 'OZ358+306'), (84.001, 'SU'), (78.001, 'SQ'), (72.003, 'TG'), (78.002, 'VN'), (109.201, 'VN503\u7559\u5b88'), (93.601, 'VN549')], max_length=10, verbose_name='\u5916\u822a')),
                ('taskclass', models.FloatField(choices=[(0.0, '\u65e0'), (1.3, '\u7ec4\u957f + F/C\u8231'), (1.2, 'F/C\u8231'), (1.1, 'Y\u8231')], default=0.0, max_length=4, verbose_name='\u4efb\u52a1\u8231\u4f4d')),
                ('taskone', models.FloatField(choices=[(0.0, '\u65e0'), (10.001, '\u7ed3\u5173\uff08\u81f3\u8fb9\u68c0\uff09'), (15.001, '\u9001\u673a\uff08\u81f3\u673a\u53e3\uff09')], default=0.0, max_length=8, verbose_name='\u7ed3\u9001\u673a')),
                ('tasktwo', models.FloatField(choices=[(0.0, '\u65e0'), (10.002, '\u6570\u7968'), (10.003, '\u7535\u62a5'), (10.004, '\u62c9Q'), (20.001, 'PRE-FLT'), (20.002, 'POST-FLT')], default=0.0, max_length=8, verbose_name='\u4e3b\u8981\u4efb\u52a11')),
                ('taskthree', models.FloatField(choices=[(0.0, '\u65e0'), (10.002, '\u6570\u7968'), (10.003, '\u7535\u62a5'), (10.004, '\u62c9Q'), (20.001, 'PRE-FLT'), (20.002, 'POST-FLT')], default=0.0, max_length=8, verbose_name='\u4e3b\u8981\u4efb\u52a12')),
                ('taskfour', models.FloatField(choices=[(0.0, '\u65e0'), (10.002, '\u6570\u7968'), (10.003, '\u7535\u62a5'), (10.004, '\u62c9Q'), (20.001, 'PRE-FLT'), (20.002, 'POST-FLT')], default=0.0, max_length=8, verbose_name='\u4e3b\u8981\u4efb\u52a13')),
                ('taskfive', models.FloatField(choices=[(0.0, '\u65e0'), (0.501, '\u52a0\u5916\u822a\u67dc\u53f0\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u65f6\u957f\uff0c\u5355\u4f4d\u201c\u5c0f\u65f6\u201d\uff09'), (0.502, '\u5ef6\u8bef\u7559\u5b88\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u65f6\u957f\uff0c\u5355\u4f4d\u201c\u5c0f\u65f6\u201d\uff09'), (5.001, '\u5916\u822a\u6311\u884c\u674e\u4ef6\u6570\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u4ef6\u6570\uff0c\u5355\u4f4d\u201c\u4ef6/\u6bcf\u6b21\u201d\uff09'), (15.002, '\u8d27\u673a\u7ed3\u5173\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u73ed\u6b21\uff0c\u53ea\u5141\u8bb8\u6574\u6570\uff0c\u5355\u4f4d\u201c\u73ed\u201d\uff09')], default=0.0, max_length=8, verbose_name='\u5176\u4ed6\u4efb\u52a1')),
                ('task_values', models.FloatField(default=0, max_length=4, verbose_name='\u6570\u503c')),
                ('other_workload', models.FloatField(default=0.0, max_length=8, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('other_point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
                ('other_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
                ('other_verify', models.CharField(choices=[('\u7b49\u5f85\u5ba1\u6838', '\u7b49\u5f85\u5ba1\u6838'), ('\u672a\u901a\u8fc7', '\u672a\u901a\u8fc7'), ('\u5df2\u5ba1\u6838', '\u5df2\u5ba1\u6838')], default='\u7b49\u5f85\u5ba1\u6838', max_length=10, verbose_name='\u5ba1\u6838\u72b6\u6001')),
                ('other_auth', models.CharField(default='NULL', max_length=8, verbose_name='\u5ba1\u6838\u4eba')),
                ('other_verifydate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u63d0\u4ea4/\u5ba1\u6838\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5916\u822a\u7ee9\u6548',
                'verbose_name_plural': '\u5916\u822a\u7ee9\u6548\u767b\u8bb0',
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='\u59d3\u540d')),
                ('team', models.CharField(choices=[('\u5168\u90e8', '\u5168\u90e8'), ('\u4e00\u5ba4', '\u4e00\u5ba4'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4'), ('\u4e09\u5ba4', '\u4e09\u5ba4'), ('\u56e2\u961f', '\u56e2\u961f')], max_length=4, verbose_name='\u5ba4\u522b')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u8d77\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u622a\u6b62\u65e5\u671f')),
                ('workload', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
            ],
            options={
                'verbose_name': '\u7ee9\u6548\u7edf\u8ba1',
                'verbose_name_plural': '\u7ee9\u6548\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='Countother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_name', models.CharField(max_length=8, verbose_name='\u59d3\u540d')),
                ('other_team', models.CharField(choices=[('\u5168\u90e8', '\u5168\u90e8'), ('\u4e00\u5ba4', '\u4e00\u5ba4'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4'), ('\u4e09\u5ba4', '\u4e09\u5ba4'), ('\u56e2\u961f', '\u56e2\u961f')], max_length=4, verbose_name='\u5ba4\u522b')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u8d77\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u622a\u6b62\u65e5\u671f')),
                ('other_workload', models.FloatField(default=0.0, max_length=8, verbose_name='\u7ee9\u6548\u4eba\u6570')),
                ('other_point', models.FloatField(default=0.0, max_length=4, verbose_name='\u7ee9\u6548\u52a0\u5206')),
            ],
            options={
                'verbose_name': '\u5916\u822a\u7edf\u8ba1',
                'verbose_name_plural': '\u5916\u822a\u7edf\u8ba1',
            },
        ),
    ]
