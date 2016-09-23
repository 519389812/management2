# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from django import forms
#from django.forms import ModelForm
import django.utils.timezone as timezone

# Create your models here.
type_choices = (
	('证件错/漏查验','证件错/漏查验'),
	('错接/发、漏接/发登机牌','错接/发、漏接/发登机牌'),
	('错输行李重量','错输行李重量'),
	('错输行李目的地','错输行李目的地'),
	('错减行李','错减行李'),
	('未回收销毁废旧行李牌','未回收销毁废旧行李牌'),
	('未回收生产物资','未回收生产物资'),
)

class Datalib(models.Model):
	case_id = models.AutoField(primary_key=True,verbose_name='序号')
	case_title = models.CharField(max_length=50,verbose_name='标题')
	case_type = models.CharField(max_length=30,choices=type_choices,verbose_name='类型')
	direct_liability = models.CharField(max_length=18,verbose_name='直接责任人')
	indirect_liability = models.CharField(max_length=26,verbose_name='间接责任人')
	destination = models.CharField(max_length=3,verbose_name='最终目的国家三字码')
	case_content = models.TextField(max_length=800,verbose_name='案例内容')
	case_analysis = models.TextField(max_length=800,verbose_name='原因分析')
	improvement = models.TextField(max_length=400,verbose_name='整改措施')
	date = models.DateField(default=timezone.now,verbose_name='日期')#	case_img = models.FileField(upload_to='./upload')

	def __unicode__(self):
		return u'责任人：%s | 标题：%s | 日期：%s'%(self.direct_liability,self.case_title,self.date)
		
	class Meta:
		verbose_name='案例'
		verbose_name_plural='值机案例库'

