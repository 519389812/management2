# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.
subject_choices = (
	(2.01,'G19自查合格'),
	(1.01,'G19自查不合格'),
	(2.02,'微笑服务'),
	(1.02,'微笑服务不合格'),
	(5.01,'南航表扬信'),
	(5.02,'外航表扬信'),
	(5.03,'5星'),
	(5.04,'3星'),
	(5.05,'迟到'),
	(10.01,'病假'),
	(5.06,'宣传报道'),
	(5.07,'投诉'),
	(2.03,'一般差错'),
	(5.08,'中等差错'),
	(10.02,'严重差错'),
	
)

airlinecode_choices = (
	('CZ','CZ'),
	('AF','AF'),
	('BR','BR'),
	('CI','CI'),
	('JL','JL'),
	('KA','KA'),
	('KE','KE'),
	('MH','MH'),
	('OZ','OZ'),
	('SU','SU'),
	('SQ','SQ'),
	('TG','TG'),
	('TG','TG'),
	('VN','VN'),
)

class Daily(models.Model):
	id = models.AutoField(primary_key=True,verbose_name='序号')
	date = models.DateField(default=timezone.now,verbose_name='日期')
	subject = models.FloatField(max_length=4,verbose_name='加减分项',choices=subject_choices,default=2.01)
	airlinecode = models.CharField(max_length=2,verbose_name='航空公司',choices=airlinecode_choices,default='CZ')
	nameone = models.CharField(max_length=8,verbose_name='姓名1',default='无')
	nametwo = models.CharField(max_length=8,verbose_name='姓名2',default='无')
	namethree = models.CharField(max_length=8,verbose_name='姓名3',default='无')
	namefour = models.CharField(max_length=8,verbose_name='姓名4',default='无')
	namefive = models.CharField(max_length=8,verbose_name='姓名5',default='无')
	namesix = models.CharField(max_length=8,verbose_name='姓名6',default='无')
	nameseven = models.CharField(max_length=8,verbose_name='姓名7',default='无')
	nameeight = models.CharField(max_length=8,verbose_name='姓名8',default='无')
	namenine = models.CharField(max_length=8,verbose_name='姓名9',default='无')
	nameten = models.CharField(max_length=8,verbose_name='姓名10',default='无')
	
	def __unicode__(self):
		return u'date：%s | subject: %s'%(self.date,self.subject)

	class Meta:
		verbose_name='每日自查'
		verbose_name_plural='每日自查'
