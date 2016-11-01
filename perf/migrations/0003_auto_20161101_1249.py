# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-01 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perf', '0002_auto_20161027_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='performance',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (5.0, '\u6311\u884c\u674e\u4ef6\u6570\uff08\u586b\u5199\u30101\u3011\u6b21\u6311\u884c\u674e\u7684\u4ef6\u6570\uff09'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.1, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u586b\u5199\u3010\u822a\u73ed\u6570\u3011\uff0c\u822a\u73ed\u53f7\u586b\u5199\u5728\u5907\u6ce8\u680f\uff09'), (10.1, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u586b\u5199\u3010\u822a\u73ed\u6570\u3011\uff0c\u822a\u73ed\u53f7\u586b\u5199\u5728\u5907\u6ce8\u680f\uff09'), (20.2, '\u8d85\u5927/\u5c0f\u65f6'), (20.3, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.4, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.1, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.2, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff0c\u8bf7\u5907\u6ce8\uff09'), (1.3, '\u5176\u4ed6/\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], default=0.0, max_length=4, verbose_name='\u4efb\u52a11'),
        ),
        migrations.AlterField(
            model_name='add',
            name='performancethree',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (5.0, '\u6311\u884c\u674e\u4ef6\u6570\uff08\u586b\u5199\u30101\u3011\u6b21\u6311\u884c\u674e\u7684\u4ef6\u6570\uff09'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.1, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u586b\u5199\u3010\u822a\u73ed\u6570\u3011\uff0c\u822a\u73ed\u53f7\u586b\u5199\u5728\u5907\u6ce8\u680f\uff09'), (10.1, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u586b\u5199\u3010\u822a\u73ed\u6570\u3011\uff0c\u822a\u73ed\u53f7\u586b\u5199\u5728\u5907\u6ce8\u680f\uff09'), (20.2, '\u8d85\u5927/\u5c0f\u65f6'), (20.3, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.4, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.1, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.2, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff0c\u8bf7\u5907\u6ce8\uff09'), (1.3, '\u5176\u4ed6/\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], default=0.0, max_length=4, verbose_name='\u4efb\u52a13'),
        ),
        migrations.AlterField(
            model_name='add',
            name='performancetwo',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (5.0, '\u6311\u884c\u674e\u4ef6\u6570\uff08\u586b\u5199\u30101\u3011\u6b21\u6311\u884c\u674e\u7684\u4ef6\u6570\uff09'), (20.0, '\u7f51\u4e0a\u503c\u673a/\u5c0f\u65f6'), (20.1, '\u56e2\u961f\u6258\u8fd0/\u5c0f\u65f6'), (10.0, '\u503c\u591c\u7ed3\u5173/\u73ed\uff08\u586b\u5199\u3010\u822a\u73ed\u6570\u3011\uff0c\u822a\u73ed\u53f7\u586b\u5199\u5728\u5907\u6ce8\u680f\uff09'), (10.1, '\u503c\u591c\u6570\u7968/\u6b21'), (15.0, '\u5173\u5c01/\u73ed\uff08\u586b\u5199\u3010\u822a\u73ed\u6570\u3011\uff0c\u822a\u73ed\u53f7\u586b\u5199\u5728\u5907\u6ce8\u680f\uff09'), (20.2, '\u8d85\u5927/\u5c0f\u65f6'), (20.3, '\u5361\u5927\u5305/\u5c0f\u65f6'), (20.4, 'Q\u53e3\u5f15\u5bfc/\u5c0f\u65f6'), (1.0, '\u52a0CZ\u67dc\u53f0/\u5c0f\u65f6'), (1.1, '\u5ef6\u65f6\u4e0b\u73ed/\u5c0f\u65f6'), (1.2, '\u534f\u52a9481\u5de5\u4f5c/\u5c0f\u65f6\uff08\u5982\u9000\u5173\u3001\u9001\u65c5\u5ba2\u3001\u5230B\u533a\u62ff\u884c\u674e\u7b49\uff0c\u8bf7\u5907\u6ce8\uff09'), (1.3, '\u5176\u4ed6/\u5c0f\u65f6/\u6b21/\u73ed\uff08\u8bf7\u5907\u6ce8\uff09')], default=0.0, max_length=4, verbose_name='\u4efb\u52a12'),
        ),
        migrations.AlterField(
            model_name='add',
            name='supervisor',
            field=models.CharField(choices=[('\u4e00\u5ba4', '\u4e00\u5ba4\uff08\u7f57\u5fd7\u748b\u3001\u6bdb\u601d\u5b34\u7b49\uff09'), ('\u4e8c\u5ba4', '\u4e8c\u5ba4\uff08\u59da\u79cb\u7115\u3001\u5218\u5468\u654f\u7b49\uff09'), ('\u4e09\u5ba4', '\u4e09\u5ba4\uff08\u5362\u4e98\u3001\u6e29\u5fd7\u68ee\u7b49\uff09'), ('\u56e2\u961f', '\u56e2\u961f\uff08\u5434\u73b2\u3001\u6881\u826f\u7b49\uff09')], max_length=4, verbose_name='\u6307\u6d3e\u5ba4'),
        ),
        migrations.AlterField(
            model_name='addother',
            name='airline',
            field=models.FloatField(choices=[(252.001, 'AF107'), (72.001, 'BR708'), (72.002, 'BR798'), (72.003, 'B7520'), (72.004, 'CI522'), (72.005, 'JL088'), (84.001, 'KA783'), (84.002, 'KA789'), (72.006, 'KE866'), (72.007, 'MH377'), (72.008, 'OZ370'), (72.009, 'OZ356'), (72.001, 'OZ358'), (72.0011, 'OZ306'), (108.001, 'OZ370+306'), (115.201, 'OZ356+306'), (100.801, 'OZ358+306'), (84.003, 'SU221'), (78.001, 'SQ851'), (78.002, 'SQ853'), (72.0012, 'TG669'), (72.0013, 'TG679'), (78.003, 'VN503'), (78.004, 'VN507'), (109.201, 'VN503\u7559\u5b88'), (93.601, 'VN549')], max_length=10, verbose_name='\u5916\u822a'),
        ),
        migrations.AlterField(
            model_name='addother',
            name='task_values',
            field=models.FloatField(default=0, max_length=4, verbose_name='\u989d\u5916\u4efb\u52a1\u6570\u503c'),
        ),
        migrations.AlterField(
            model_name='addother',
            name='taskfive',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (0.501, '\u52a0\u5916\u822a\u67dc\u53f0/\u5c0f\u65f6\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u65f6\u957f\uff09'), (0.503, '\u5916\u822a\u4e34\u65f6\u8c03\u4efb\u7ec4\u957f1\u6b21\uff08\u4e0b\u65b9\u65e0\u987b\u586b\u5199\u6570\u503c\uff0c\u56fa\u5b9a\u4e3a1\u6b21\uff09'), (0.502, '\u5ef6\u8bef\u7559\u5b88/\u5c0f\u65f6\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u65f6\u957f\uff09'), (5.001, '\u5916\u822a\u6311\u884c\u674e\u4ef6\u6570\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u4ef6\u6570\uff09'), (15.002, '\u8d27\u673a\u7ed3\u5173/\u73ed\uff08\u8bf7\u5728\u4e0b\u65b9\u586b\u5199\u822a\u73ed\u6570\uff0c\u53ea\u5141\u8bb8\u6574\u6570\uff09')], default=0.0, max_length=8, verbose_name='\u989d\u5916\u4efb\u52a1'),
        ),
        migrations.AlterField(
            model_name='addother',
            name='taskfour',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (10.002, '\u6570\u7968\uff08\u53ef\u9009\u5916\u822a\uff1aSU\u3001KE\uff09'), (10.003, '\u7535\u62a5'), (10.004, '\u62c9Q'), (20.001, 'PRE-FLT'), (20.002, 'POST-FLT')], default=0.0, max_length=8, verbose_name='\u4e3b\u8981\u4efb\u52a13'),
        ),
        migrations.AlterField(
            model_name='addother',
            name='taskthree',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (10.002, '\u6570\u7968\uff08\u53ef\u9009\u5916\u822a\uff1aSU\u3001KE\uff09'), (10.003, '\u7535\u62a5'), (10.004, '\u62c9Q'), (20.001, 'PRE-FLT'), (20.002, 'POST-FLT')], default=0.0, max_length=8, verbose_name='\u4e3b\u8981\u4efb\u52a12'),
        ),
        migrations.AlterField(
            model_name='addother',
            name='tasktwo',
            field=models.FloatField(choices=[(0.0, '\u65e0'), (10.002, '\u6570\u7968\uff08\u53ef\u9009\u5916\u822a\uff1aSU\u3001KE\uff09'), (10.003, '\u7535\u62a5'), (10.004, '\u62c9Q'), (20.001, 'PRE-FLT'), (20.002, 'POST-FLT')], default=0.0, max_length=8, verbose_name='\u4e3b\u8981\u4efb\u52a11'),
        ),
    ]
