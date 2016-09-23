# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django import forms
#from django.forms import ModelForm
import django.utils.timezone as timezone
from get_username import get_username

# Create your models here.
perf_choices = (
	(5.0,'挑行李   件/1次'),
	(20.0,'网上值机/小时'),
	(20.0,'团队托运/小时'),
	(10.0,'值夜结关/班（请备注航班）'),
	(10.0,'值夜数票/次'),
	(15.0,'关封/班（请备注航班）'),
	(20.0,'超大/小时'),
	(20.0,'卡大包/小时'),
	(20.0,'Q口引导/小时'),
	(1.0,'加CZ柜台/小时'),
	(1.0,'延时下班/小时'),
	(1.0,'协助481工作/小时（如退关、送旅客、到B区拿行李等）（请备注）'),
	(1.0,'其他   /小时/次/班（请备注）'),
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
	performance = models.FloatField(max_length=4,choices=perf_choices,verbose_name='项目')
	values = models.FloatField(max_length=4,verbose_name='数值')
	workload = models.FloatField(max_length=4,default=0.0,verbose_name='绩效人数')
	point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')
	date = models.DateField(default=timezone.now,verbose_name='日期')
	verify = models.CharField(max_length=10,default='等待审核',choices=verify_choices,verbose_name='审核状态')
	verify_auth = models.CharField(max_length=8,verbose_name='审核人',null=True,blank=True)
	verify_date = models.DateTimeField(verbose_name='提交/审核时间',default=timezone.now)
	comment = models.TextField(max_length=40,default='无',verbose_name='备注')
		
	def __unicode__(self):
		return u'%s>>>>%s>>>>%s>>>>%s>>>>%s>>>>%s'%(self.name,self.team,self.workload,self.point,self.date,self.verify)

	def save(self, *args, **kwargs):
		req = get_username()
#		print "Your username is : %s" %(req.user)
		if self.verify == '等待审核':
			super(Add, self).save(*args, **kwargs) # Call the "real" save() method.
		if self.verify == '已审核':
			self.verify_auth = str(req.user)
			self.verify_date = timezone.now()
			super(Add, self).save(*args, **kwargs) # Call the "real" save() method.
		if self.verify == '未通过审核':
			self.verify_auth = str(req.user)
			self.verify_date = timezone.now()
			super(Add, self).save(*args, **kwargs) # Call the "real" save() method.

	class Meta:
		verbose_name='绩效'
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
		verbose_name='绩效统计'
		verbose_name_plural='绩效统计'