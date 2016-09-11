# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django import forms
#from django.forms import ModelForm
import django.utils.timezone as timezone

# Create your models here.
perf_choices = (
	(15.0,'加柜台/小时'),
	(5.0,'挑行李/件'),
	(20.0,'协助481/小时'),
	(10.0,'结关/班'),
)

team_choices = (
	('一室','一室'),
	('二室','二室'),
	('三室','三室'),
	('团队','团队'),
)

verify_choices = (
	('等待审核','等待审核'),
	('未通过审核','未通过审核'),
	('已审核','已审核'),
)


class Add(models.Model):
	perf_id = models.AutoField(primary_key=True,verbose_name='序号')
	name = models.CharField(max_length=8,verbose_name='姓名')
	team = models.CharField(max_length=4,choices=team_choices,verbose_name='室别')
	performance = models.FloatField(max_length=4,choices=perf_choices,verbose_name='加分项')
	values = models.FloatField(max_length=4,verbose_name='数值')
	workload = models.FloatField(max_length=4,default=0.0,verbose_name='绩效人数')
	point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')
	date = models.DateField(default=timezone.now,verbose_name='日期')
	verify = models.CharField(max_length=8,default='等待审核',choices=verify_choices,verbose_name='审核状态')
		
	def __unicode__(self):
		return u'%s>>>>%s>>>>%s>>>>%s>>>>%s>>>>%s'%(self.name,self.team,self.workload,self.point,self.date,self.verify)
		
	class Meta:
		verbose_name='摘要'
		verbose_name_plural='绩效登记'

year_choices = (
	(2016,'2016'),
	#(2017,'2017'),
)

month_choices = (
	(1,'01'),
	(2,'02'),
	(3,'03'),
	(4,'04'),
	(5,'05'),
	(6,'06'),
	(7,'07'),
	(8,'08'),
	(9,'09'),
	(10,'10'),
	(11,'11'),
	(12,'12'),
)

class Count(models.Model):
	name = models.CharField(max_length=8,verbose_name='姓名')
	team = models.CharField(max_length=4,choices=team_choices,verbose_name='室别')
	year = models.IntegerField(verbose_name='年份',choices=year_choices)
	month = models.IntegerField(verbose_name='月份',choices=month_choices)
	workload = models.FloatField(max_length=4,default=0.0,verbose_name='绩效人数')
	point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')

	
	def __unicode__(self):
		return u'%s>>>>%s>>>>%s>>>>%s>>>>%s'%(self.name,self.team,self.workload,self.point,self.date)
		
	class Meta:
		verbose_name='摘要'
		verbose_name_plural='绩效统计'