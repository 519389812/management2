# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from django import forms
#from django.forms import ModelForm
import django.utils.timezone as timezone

# Create your models here.
type_choices = (
	('值机差错','值机差错'),
	('行李托运','行李托运'),
)

class Datalib(models.Model):
	case_id = models.AutoField(primary_key=True,verbose_name='序号')
	case_title = models.CharField(max_length=30,verbose_name='标题')
	case_type = models.CharField(max_length=10,choices=type_choices,verbose_name='类型')
	direct_liability = models.CharField(max_length=18,verbose_name='直接责任人')
	indirect_liability = models.CharField(max_length=26,verbose_name='管理责任人')
	case_content = models.TextField(max_length=800,verbose_name='案例内容')
	case_analysis = models.TextField(max_length=800,verbose_name='原因分析')
	improvement = models.TextField(max_length=400,verbose_name='整改措施')
	date = models.DateField(default=timezone.now,verbose_name='日期')

	def __unicode__(self):
		return u'责任人：%s>>>>>>标题：%s>>>>>>日期：%s'%(self.direct_liability,self.case_title,self.date)
		
	class Meta:
		verbose_name='摘要'
		verbose_name_plural='值机案例库'

