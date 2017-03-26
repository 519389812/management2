# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-25 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u5e8f\u53f7')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
                ('subject', models.FloatField(choices=[(2.01, 'G19\u81ea\u67e5\u5408\u683c'), (1.01, 'G19\u81ea\u67e5\u4e0d\u5408\u683c'), (2.02, '\u5fae\u7b11\u670d\u52a1'), (1.02, '\u5fae\u7b11\u670d\u52a1\u4e0d\u5408\u683c'), (5.01, '\u5357\u822a\u8868\u626c\u4fe1'), (5.02, '\u5916\u822a\u8868\u626c\u4fe1'), (5.03, '5\u661f'), (5.04, '3\u661f'), (5.05, '\u8fdf\u5230'), (10.01, '\u75c5\u5047'), (5.06, '\u5ba3\u4f20\u62a5\u9053'), (5.07, '\u6295\u8bc9'), (2.03, '\u4e00\u822c\u5dee\u9519'), (5.08, '\u4e2d\u7b49\u5dee\u9519'), (10.02, '\u4e25\u91cd\u5dee\u9519')], default=2.01, max_length=4, verbose_name='\u52a0\u51cf\u5206\u9879')),
                ('airlinecode', models.CharField(choices=[('CZ', 'CZ'), ('AF', 'AF'), ('BR', 'BR'), ('CI', 'CI'), ('JL', 'JL'), ('KA', 'KA'), ('KE', 'KE'), ('MH', 'MH'), ('OZ', 'OZ'), ('SU', 'SU'), ('SQ', 'SQ'), ('TG', 'TG'), ('TG', 'TG'), ('VN', 'VN')], default='CZ', max_length=2, verbose_name='\u822a\u7a7a\u516c\u53f8')),
                ('nameone', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d1')),
                ('nametwo', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d2')),
                ('namethree', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d3')),
                ('namefour', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d4')),
                ('namefive', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d5')),
                ('namesix', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d6')),
                ('nameseven', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d7')),
                ('nameeight', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d8')),
                ('namenine', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d9')),
                ('nameten', models.CharField(default='\u65e0', max_length=8, verbose_name='\u59d3\u540d10')),
            ],
            options={
                'verbose_name': '\u6bcf\u65e5\u81ea\u67e5',
                'verbose_name_plural': '\u6bcf\u65e5\u81ea\u67e5',
            },
        ),
    ]