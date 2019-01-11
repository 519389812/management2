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


class Staff(models.Model):
	id = models.AutoField(primary_key=True,verbose_name='序号')
	name = models.CharField(max_length=8,unique=True,verbose_name='姓名')
	group = models.CharField(max_length=8,choices=group_choices,verbose_name='团队')

		
	def __unicode__(self):
		return u'姓名：%s | 工号：%s'%(self.name,self.group)

	class Meta:
		verbose_name='员工档案'
		verbose_name_plural='员工档案'