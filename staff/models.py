# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
group_choices = (
	('一室1组','一室1组'),
	('一室2组','一室2组'),
	('一室3组','一室3组'),
	('二室4组','二室4组'),
	('二室5组','二室5组'),
	('二室6组','二室6组'),
	('三室7组','三室7组'),
	('三室8组','三室8组'),
	('三室9组','三室9组'),
	('团队1组','团队1组'),
	('团队2组','团队2组'),
	('团队3组','团队3组'),
)

bool_choices = (
	(0,'N'),
	(1,'Y'),
)

status_choices = (
	('在职','在职'),
	('借调','借调'),
	('病产假','病产假'),
	('离职','离职'),
)

class Staff(models.Model):
	id = models.AutoField(primary_key=True,verbose_name='序号')
	name = models.CharField(max_length=8,verbose_name='姓名')
	eid = models.IntegerField(verbose_name='员工号')
	wid = models.IntegerField(verbose_name='工作号')
	group = models.CharField(max_length=8,choices=group_choices,verbose_name='团队')
	birth = models.DateField(verbose_name='生日')
	eqmanage = models.IntegerField(choices=bool_choices,verbose_name='设备管理',default=0)
	assistant = models.IntegerField(choices=bool_choices,verbose_name='外航助理',default=0)
	groupleader = models.IntegerField(choices=bool_choices,verbose_name='组长',default=0)
	typing = models.IntegerField(choices=bool_choices,verbose_name='打字',default=0)
	counting = models.IntegerField(choices=bool_choices,verbose_name='数票',default=0)
	accountmanage = models.IntegerField(choices=bool_choices,verbose_name='财务',default=0)
	courseware = models.IntegerField(choices=bool_choices,verbose_name='课件制作',default=0)
	af = models.IntegerField(choices=bool_choices,default=0)
	br = models.IntegerField(choices=bool_choices,default=0)
	ci = models.IntegerField(choices=bool_choices,default=0)
	jl = models.IntegerField(choices=bool_choices,default=0)
	ka = models.IntegerField(choices=bool_choices,default=0)
	ke = models.IntegerField(choices=bool_choices,default=0)
	mh = models.IntegerField(choices=bool_choices,default=0)
	oz = models.IntegerField(choices=bool_choices,default=0)
	su = models.IntegerField(choices=bool_choices,default=0)
	sq = models.IntegerField(choices=bool_choices,default=0)
	tg = models.IntegerField(choices=bool_choices,default=0)
	vn = models.IntegerField(choices=bool_choices,default=0)
	status = models.CharField(max_length=4,choices=status_choices,verbose_name='状态')
		
	def __unicode__(self):
		return u'姓名：%s | 工号：%s | 室组：%s'%(self.name,self.eid,self.group)

	class Meta:
		verbose_name='员工档案'
		verbose_name_plural='员工档案'