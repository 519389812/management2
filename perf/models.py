# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django import forms
#from django.forms import ModelForm
import django.utils.timezone as timezone
from get_username import get_username

# Create your models here.
perf_choices = (
	(0.0,'无'),
	(5.0,'挑行李件数（填写【1】次挑行李的件数）'),
	(20.0,'网上值机/小时'),
	(20.1,'团队托运/小时'),
	(10.0,'值夜结关/班（【航班号】填写在备注栏）'),
	(30.1,'顶替481巡视或471/小时'),
	(15.0,'关封/班（【航班号】填写在备注栏）'),
	(20.2,'顶替超大/小时'),
	(20.3,'协助结关/小时'),
	(20.4,'Q口引导/小时'),
	(1.0,'加CZ柜台/小时'),
	(1.1,'延时下班/小时'),
	(1.2,'带晚到旅客/次'),
	(1.3,'带旅客去行查/次'),
	(1.4,'协助退关/次'),
	(1.5,'到达取行李/次'),
	(1.6,'拿宵夜/次'),
	(1.7,'其他/次（请备注）'),
)

verify_choices = (
	('等待审核','等待审核'),
	('未通过','未通过'),
	('已审核','已审核'),
)

supervisor_choices = (
	('一室','一室'),
	('二室','二室'),
	('三室','三室'),
	('团队','团队'),
)

class Add(models.Model):
	perf_id = models.AutoField(primary_key=True,verbose_name='序号')
	name = models.CharField(max_length=8,verbose_name='姓名')
	team = models.CharField(max_length=8,verbose_name='室别',editable=False)
	performance = models.FloatField(max_length=4,choices=perf_choices,verbose_name='任务1',default=0.0)
	values = models.FloatField(max_length=4,verbose_name='数值1',default=0)
	performancetwo = models.FloatField(max_length=4,choices=perf_choices,verbose_name='任务2',default=0.0)
	valuestwo = models.FloatField(max_length=4,verbose_name='数值2',default=0)
	performancethree = models.FloatField(max_length=4,choices=perf_choices,verbose_name='任务3',default=0.0)
	valuesthree = models.FloatField(max_length=4,verbose_name='数值3',default=0)
	workload = models.FloatField(max_length=4,default=0.0,verbose_name='绩效人数')
	point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')
	supervisor = models.CharField(max_length=4,choices=supervisor_choices,verbose_name='指派室')
	date = models.DateField(default=timezone.now,verbose_name='日期')
	verify = models.CharField(max_length=10,default='等待审核',choices=verify_choices,verbose_name='审核状态')
	verify_auth = models.CharField(max_length=8,verbose_name='审核人',default='NULL')
	verify_date = models.DateTimeField(verbose_name='提交/审核时间',default=timezone.now)
	comment = models.TextField(max_length=40,default='无',verbose_name='备注')
		
	def __unicode__(self):
		return u'姓名：%s | 工作量：%s | 加分：%s | 指派室：%s | 日期：%s | 审核状态：%s'%(self.name,self.workload,self.point,self.supervisor,self.date,self.verify)

	def save(self, *args, **kwargs):
		req = get_username()
#		print "Your username is : %s" %(req.user)
		if self.verify == '等待审核':
			super(Add, self).save(*args, **kwargs) # Call the "real" save() method.
		if self.verify == '已审核':
			self.verify_auth = str(req.user)
			self.verify_date = timezone.now()
			super(Add, self).save(*args, **kwargs) # Call the "real" save() method.
		if self.verify == '未通过':
			self.verify_auth = str(req.user)
			self.verify_date = timezone.now()
			super(Add, self).save(*args, **kwargs) # Call the "real" save() method.

	class Meta:
		verbose_name='南航绩效'
		verbose_name_plural='南航绩效'


#-------------------------------------------------------------------------------------#

taskone_choices = (
	(0.0,'无'),
	(10.001,'结关（至边检）'),
	(15.001,'送机（至机口）'),
)

tasktwo_choices = (
	(0.0,'无'),
	(10.002,'数票（仅：SU、KE）'),
	(10.003,'电报'),
	(10.004,'拉Q'),
	(20.001,'PRE-FLT'),
	(20.002,'POST-FLT'),
	(20.003,'带机组（仅3U）'),
	(20.004,'推上'),
)

taskthree_choices = (
	(0.0,'无'),
	(0.501,'加外航柜台/小时（请在下方填写时长）'),
	(0.502,'延误留守/小时（请在下方填写时长）'),
	(0.503,'临时调任外航组长1次（下方无须填写数值，固定为1次）'),
	(5.001,'外航挑行李件数（请在下方填写件数）'),
	(15.002,'货机结关/班（请在下方填写航班数，只允许整数）'),
	(0.504,'不上柜台，临时调配带机组1次（下方无须填写数值，固定为1次）'),
)

class_choices = (
	(0.0,'无'),
	(1.3,'组长 + F/C舱'),
	(1.2,'F/C舱'),
	(1.1,'Y舱'),
)

airline_choices = (
	(252.0001,'AF107'),
	(72.0001,'BR708'),
	(72.0002,'BR798'),
	(72.0003,'B7520'),
	(72.0004,'CI522'),
	(72.0005,'JL088'),
	(112.0001,'KA789早上柜台'),
	(84.0001,'KA783'),
	(84.0002,'KA789'),
	(72.0006,'KE866'),
	(72.0007,'MH377'),
	(72.0008,'午OZ370'),
	(72.0009,'晚OZ356'),
	(72.0011,'晚OZ358'),
	(72.0012,'午OZ306'),
	(72.0015,'晚OZ306'),
	(108.0001,'午OZ370+午306'),
	(115.2001,'晚OZ356+晚306'),
	(100.8001,'晚OZ358+晚306'),
	(84.0003,'SU221'),
	(78.0001,'SQ851'),
	(78.0002,'SQ853'),
	(72.0013,'TG669'),
	(72.0014,'TG679'),
	(78.0003,'VN503'),
	(78.0004,'VN507'),
	(109.2001,'VN503留守'),
	(93.6001,'VN549'),
	(19.24,'3U川航'),
)

verify_choices = (
	('等待审核','等待审核'),
	('未通过','未通过'),
	('已审核','已审核'),
)

class Addother(models.Model):
	other_id = models.AutoField(primary_key=True,verbose_name='序号')
	other_name = models.CharField(max_length=8,verbose_name='姓名')
	other_team = models.CharField(max_length=8,verbose_name='室别',editable=False)
	airline = models.FloatField(max_length=10,choices=airline_choices,verbose_name='外航')
	taskclass = models.FloatField(max_length=4,choices=class_choices,verbose_name='任务舱位',default=0.0)
	taskone = models.FloatField(max_length=8,choices=taskone_choices,verbose_name='结送机',default=0.0)
	tasktwo = models.FloatField(max_length=8,choices=tasktwo_choices,verbose_name='主要任务1',default=0.0)
	taskthree = models.FloatField(max_length=8,choices=tasktwo_choices,verbose_name='主要任务2',default=0.0)
	taskfour = models.FloatField(max_length=8,choices=tasktwo_choices,verbose_name='主要任务3',default=0.0)
	taskfive = models.FloatField(max_length=8,choices=taskthree_choices,verbose_name='额外任务',default=0.0)
	task_values = models.FloatField(max_length=4,verbose_name='额外任务数值',default=0)
	other_workload = models.FloatField(max_length=8,default=0.0,verbose_name='绩效人数')
	other_point = models.FloatField(max_length=4,default=0.0,verbose_name='绩效加分')
	other_date = models.DateField(default=timezone.now,verbose_name='日期')
	other_verify = models.CharField(max_length=10,default='等待审核',choices=verify_choices,verbose_name='审核状态')
	other_auth = models.CharField(max_length=8,verbose_name='审核人',default='NULL')
	other_verifydate = models.DateTimeField(verbose_name='提交/审核时间',default=timezone.now)
		
	def __unicode__(self):
		return u'姓名：%s | 外航：%s | 绩效人数：%s | 绩效加分：%s | 日期：%s | 审核状态：%s'%(self.other_name,self.airline,self.other_workload,self.other_point,self.other_date,self.other_verify)

	def save(self, *args, **kwargs):
		req = get_username()
#		print "Your username is : %s" %(req.user)
		if self.other_verify == '等待审核':
			super(Addother, self).save(*args, **kwargs) # Call the "real" save() method.
		if self.other_verify == '已审核':
			self.other_auth = str(req.user)
			self.other_verifydate = timezone.now()
			super(Addother, self).save(*args, **kwargs) # Call the "real" save() method.
		if self.other_verify == '未通过':
			self.other_auth = str(req.user)
			self.other_verifydate = timezone.now()
			super(Addother, self).save(*args, **kwargs) # Call the "real" save() method.

	class Meta:
		verbose_name='外航绩效'
		verbose_name_plural='外航绩效'
