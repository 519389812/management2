# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Count(models.Model):
	name = models.CharField(max_length=8,verbose_name='姓名')
	team = models.CharField(max_length=4,verbose_name='室别')
	start_date = models.DateField(default=timezone.now,verbose_name='起始日期')
	end_date = models.DateField(default=timezone.now,verbose_name='截止日期')
	workload = models.FloatField(max_length=4,default=0.0,verbose_name='绩效人数')
	point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')

	
	def __unicode__(self):
		return u'%s|%s|%s|%s'%(self.name,self.team,self.start_date,self.end_date)
		
	class Meta:
		verbose_name='绩效统计'
		verbose_name_plural='绩效统计'


class Countother(models.Model):
	other_name = models.CharField(max_length=8,verbose_name='姓名')
	other_team = models.CharField(max_length=4,verbose_name='室别')
	start_date = models.DateField(default=timezone.now,verbose_name='起始日期')
	end_date = models.DateField(default=timezone.now,verbose_name='截止日期')
	other_workload = models.FloatField(max_length=8,default=0.0,verbose_name='绩效人数')
	other_point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')
	ci = models.IntegerField(default=0,verbose_name='ci次数')
	ka = models.IntegerField(default=0,verbose_name='ka次数')
	customsoz = models.IntegerField(default=0,verbose_name='oz结关')
	customssq = models.IntegerField(default=0,verbose_name='sq结关')
	postsq = models.IntegerField(default=0,verbose_name='sq-post')
	
	def __unicode__(self):
		return u'%s|%s|%s|%s'%(self.other_name,self.other_team,self.start_date,self.end_date)
		
	class Meta:
		verbose_name='外航统计'
		verbose_name_plural='外航统计'


class Ranking(models.Model):
	id = models.AutoField(primary_key=True,verbose_name='序号')
	name = models.CharField(max_length=8,verbose_name='姓名')
	eid = models.IntegerField(verbose_name='员工号')
	wid = models.IntegerField(verbose_name='工作号')
	group = models.CharField(max_length=8,verbose_name='团队')
	eqmanage = models.IntegerField(verbose_name='设备管理',default=0)
	assistant = models.IntegerField(verbose_name='外航助理',default=0)
	groupleader = models.IntegerField(verbose_name='组长',default=0)
	typing = models.IntegerField(verbose_name='打字',default=0)
	counting = models.IntegerField(verbose_name='数票',default=0)
	accountmanage = models.IntegerField(verbose_name='财务',default=0)
	courseware = models.IntegerField(verbose_name='课件制作',default=0)
	skill = models.IntegerField(verbose_name='技能数',default=0)
	spoints = models.IntegerField(verbose_name='技能加分',default=0)
	selfchecky = models.IntegerField(verbose_name='自查合格',default=0)
	selfcheckn = models.IntegerField(verbose_name='自查不合格',default=0)
	scpoints = models.IntegerField(verbose_name='自查得分',default=0)
	smileservy = models.IntegerField(verbose_name='微笑合格',default=0)
	smileservn = models.IntegerField(verbose_name='微笑不合格',default=0)
	sspoints = models.IntegerField(verbose_name='微笑得分',default=0)
	cspraiseletters = models.IntegerField(verbose_name='南航表扬信',default=0)
	othpraiseletters = models.IntegerField(verbose_name='外航表扬信',default=0)
	plpoints = models.IntegerField(verbose_name='表扬信得分',default=0)
	fivestars = models.IntegerField(verbose_name='五星',default=0)
	threestars = models.IntegerField(verbose_name='三星',default=0)
	starpoints = models.IntegerField(verbose_name='五星得分',default=0)
	lateshow = models.IntegerField(verbose_name='迟到',default=0)
	lspoints = models.IntegerField(verbose_name='迟到扣分',default=0)
	sickleave = models.IntegerField(verbose_name='病假',default=0)
	slpoints = models.IntegerField(verbose_name='病假扣分',default=0)
	fullattendance = models.IntegerField(verbose_name='全勤',default=2)
	publicity = models.IntegerField(verbose_name='宣传报道',default=0)
	ppoints = models.IntegerField(verbose_name='宣传报道得分',default=0)
	complaint = models.IntegerField(verbose_name='投诉',default=0)
	cpoints = models.IntegerField(verbose_name='投诉扣分',default=0)
	nocomplaint = models.IntegerField(verbose_name='无投诉',default=1)
	mistakelv1 = models.IntegerField(verbose_name='一般差错',default=0)
	mistakelv2 = models.IntegerField(verbose_name='中等差错',default=0)
	mistakelv3 = models.IntegerField(verbose_name='严重差错',default=0)
	mtpoints = models.IntegerField(verbose_name='差错扣分',default=0)
	nomistake = models.IntegerField(verbose_name='无差错',default=5)
	total = models.IntegerField(verbose_name='最终得分',default=0)
	date = models.DateField(verbose_name='起始时间',default=timezone.now)
	end_date = models.DateField(verbose_name='截止时间',default=timezone.now)

	def __unicode__(self):
		return u'start_date：%s | end_date: %s  '%(self.date,self.end_date)

	class Meta:
		verbose_name='个人得分'
		verbose_name_plural='个人得分'
