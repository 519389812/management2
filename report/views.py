# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from perf.models import Add,Addother
from report.models import Count,Countother,Ranking
from administrator.models import Daily
from perf.forms import AddForm,AddotherForm
from report.forms import CountForm,CountotherForm,RankingForm
from administrator.forms import DailyForm
from staff.models import Staff
from staff.forms import StaffForm
import sqlite3
import sys
#from __future__ import unicode_literals
from django.http import JsonResponse
import xlwt
from cStringIO import StringIO
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime
import time
from collections import defaultdict
from django.utils.timezone import now, timedelta


# Create your views here.
def count(req):
	if req.method == 'POST':
		form = CountForm(req.POST)
		if form.is_valid():
			date_from = form.cleaned_data['start_date']
			date_until = form.cleaned_data['end_date']
			if len(Count.objects.all())>0:
				Count.objects.all().delete()
			sets = Add.objects.filter(date__range=(date_from,date_until),verify = '已审核')
			for set in sets:
				if len(Count.objects.filter(name = set.name))>0:
					get = Count.objects.get(name = set.name)
					get.workload = get.workload + set.workload
					get.point = get.point + set.point
					get.save()
				else:
					getteam = Staff.objects.get(name=set.name)
					create = Count(name=set.name,team=getteam.group,workload=set.workload,point=set.point,start_date=date_from,end_date=date_until)
					create.save()
			return HttpResponseRedirect('/excel_download/')
	else:
		form = CountForm()
	return render(req,'count.html',{'form':form})

	
def countother(req):
	if req.method == 'POST':
		form = CountotherForm(req.POST)
		if form.is_valid():
			Countother.objects.all().delete()
			date_from = form.cleaned_data['start_date']
			date_until = form.cleaned_data['end_date']
			if len(Count.objects.all())>0:
				Countother.objects.all().delete()
			sets = Addother.objects.filter(other_date__range=(date_from,date_until),other_verify = '已审核')
			for set in sets:
				if len(Countother.objects.filter(other_name = set.other_name))>0:
					get = Countother.objects.get(other_name = set.other_name)
					get.other_workload = get.other_workload + set.other_workload
					get.other_point = get.other_point + set.other_point
					if set.airline == 72.0004:
						get.ci += 1
					if set.airline == 84.0001:
						get.ka += 1
					if set.airline == 84.0002:
						get.ka += 1
					if set.airline == 112.0001:
						get.ka += 1
					if set.airline == 72.0009 and set.taskone == 10.001:
						get.customsoz += 1
					if set.airline == 72.0011 and set.taskone == 10.001:
						get.customsoz += 1
					if set.airline == 72.0015 and set.taskone == 10.001:
						get.customsoz += 1
					if set.airline == 115.2001 and set.taskone == 10.001:
						get.customsoz += 1
					if set.airline == 100.8001 and set.taskone == 10.001:
						get.customsoz += 1
					if set.airline == 78.0002 and set.taskone == 15.001:
						get.customssq += 1
					if set.airline == 78.0002 and set.taskone == 10.001:
						get.customssq += 1
					if set.airline == 78.0002 and set.tasktwo == 20.002:
						get.postsq += 1
					if set.airline == 78.0002 and set.taskthree == 20.002:
						get.postsq += 1
					if set.airline == 78.0002 and set.taskfour == 20.002:
						get.postsq += 1
					get.save()
				else:
					colci = 0
					colka = 0
					colcustomsoz = 0
					colcustomssq = 0
					colpostsq = 0
					getteam = Staff.objects.get(name=set.other_name)
					if set.airline == 72.0004:
						colci += 1
					if set.airline == 84.0001:
						colka += 1
					if set.airline == 84.0002:
						colka += 1
					if set.airline == 112.0001:
						colka += 1
					if set.airline == 72.0009 and set.taskone == 10.001:
						colcustomsoz += 1
					if set.airline == 72.0011 and set.taskone == 10.001:
						colcustomsoz += 1
					if set.airline == 72.0015 and set.taskone == 10.001:
						colcustomsoz += 1
					if set.airline == 115.2001 and set.taskone == 10.001:
						colcustomsoz += 1
					if set.airline == 100.8001 and set.taskone == 10.001:
						colcustomsoz += 1
					if set.airline == 78.0002 and set.taskone == 15.001:
						colcustomssq += 1
					if set.airline == 78.0002 and set.taskone == 10.001:
						colcustomssq += 1
					if set.airline == 78.0002 and set.tasktwo == 20.002:
						colpostsq += 1
					if set.airline == 78.0002 and set.taskthree == 20.002:
						colpostsq += 1
					if set.airline == 78.0002 and set.taskfour == 20.002:
						colpostsq += 1
					create = Countother(other_name=set.other_name,other_team=getteam.group,other_workload=set.other_workload,other_point=set.other_point,start_date=date_from,end_date=date_until,ci=colci,ka=colka,customsoz=colcustomsoz,customssq=colcustomssq,postsq=colpostsq)
					create.save()
			return HttpResponseRedirect('/other_download/')
	else:
		form = CountotherForm()
	return render(req,'countother.html',{'form':form})

	
def count_output(req):
	wb = xlwt.Workbook(encoding = 'utf-8')
	sheet = wb.add_sheet(u'统计')
	
	font0 = xlwt.Font()
	font0.colour_index = 2
	font0.bold = True
	font0.height = 0x258
	
	alignment1 = xlwt.Alignment()
	alignment1.horz = xlwt.Alignment.HORZ_CENTER
	alignment1.vert = xlwt.Alignment.VERT_CENTER
	
	font1 = xlwt.Font()
	font1.colour_index = 4
	font1.bold = True
	
	font2 = xlwt.Font()
	font2.colour_index = 2
	
	font3 = xlwt.Font()
	font3.colour_index = 3
	
	style0 = xlwt.XFStyle()
	style0.font = font0
	style0.alignment = alignment1
	
	style1 = xlwt.XFStyle()
	style1.font = font1
	
	style2 = xlwt.XFStyle()
	style2.font = font2
	
	style3 = xlwt.XFStyle()
	style3.font = font3
	
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment;filename=南航绩效统计.xls'
	
	sheet.write_merge(0,0,0,5,'南航绩效统计',style0)
	
	sheet.write(1,0, '姓名')
	sheet.write(1,1, '室别')
	sheet.write(1,2, '工作量')
	sheet.write(1,3, '绩效加分')
	sheet.write(1,4, '起始日期')
	sheet.write(1,5, '截止日期')
	
	row = 2
	for count in Count.objects.order_by('team'):
		sheet.write(row,0, count.name,style1)
		sheet.write(row,1, count.team)
		sheet.write(row,2, count.workload,style2)
		sheet.write(row,3, count.point,style2)
		sheet.write(row,4, str(count.start_date))
		sheet.write(row,5, str(count.end_date))
		row = row + 1

	output = StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response

	
def other_output(req):
	wb = xlwt.Workbook(encoding = 'utf-8')
	sheet = wb.add_sheet(u'统计')
	
	font0 = xlwt.Font()
	font0.colour_index = 2
	font0.bold = True
	font0.height = 0x258
	
	alignment1 = xlwt.Alignment()
	alignment1.horz = xlwt.Alignment.HORZ_CENTER
	alignment1.vert = xlwt.Alignment.VERT_CENTER
	
	font1 = xlwt.Font()
	font1.colour_index = 4
	font1.bold = True
	
	font2 = xlwt.Font()
	font2.colour_index = 2
	
	font3 = xlwt.Font()
	font3.colour_index = 3
	
	style0 = xlwt.XFStyle()
	style0.font = font0
	style0.alignment = alignment1
	
	style1 = xlwt.XFStyle()
	style1.font = font1
	
	style2 = xlwt.XFStyle()
	style2.font = font2
	
	style3 = xlwt.XFStyle()
	style3.font = font3
	
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment;filename=外航绩效统计.xls'
	
	sheet.write_merge(0,0,0,10,'外航绩效统计',style0)
	
	sheet.write(1,0, '姓名')
	sheet.write(1,1, '室别')
	sheet.write(1,2, '工作量')
	sheet.write(1,3, '加分')
	sheet.write(1,4, 'CI次数')
	sheet.write(1,5, 'KA次数')
	sheet.write(1,6, 'OZ结关次数')
	sheet.write(1,7, 'SQ结关次数')
	sheet.write(1,8, 'SQ POST次数')
	sheet.write(1,9, '起始日期')
	sheet.write(1,10, '截止日期')
	
	row = 2
	for countother in Countother.objects.order_by('other_team'):
		sheet.write(row,0, countother.other_name,style1)
		sheet.write(row,1, countother.other_team)
		sheet.write(row,2, countother.other_workload,style2)
		sheet.write(row,3, countother.other_point,style2)
		sheet.write(row,4, countother.ci)
		sheet.write(row,5, countother.ka)
		sheet.write(row,6, countother.customsoz)
		sheet.write(row,7, countother.customssq)
		sheet.write(row,8, countother.postsq)
		sheet.write(row,9, str(countother.start_date))
		sheet.write(row,10, str(countother.end_date))
		row = row + 1

	output = StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response

def ranking(req):
	dictdaily = {}
	if req.method == 'POST':
		form = RankingForm(req.POST)
		if form.is_valid():
			date_from = form.cleaned_data['date']
			date_until = form.cleaned_data['end_date']
			Ranking.objects.all().delete()
			getstaff = Staff.objects.all()
			for get in getstaff:
				create = Ranking(name=get.name,eid=get.eid,wid=get.wid,group=get.group,eqmanage=get.eqmanage*10,assistant=get.assistant*10,groupleader=get.groupleader*10,typing=get.typing,counting=get.counting,accountmanage=get.accountmanage,courseware=get.courseware*10,skill=get.af+get.br+get.ci+get.jl+get.ka+get.ke+get.mh+get.oz+get.su+get.sq+get.tg+get.vn,spoints=0,selfchecky=0,selfcheckn=0,scpoints=0,smileservy=0,smileservn=0,sspoints=0,cspraiseletters=0,othpraiseletters=0,plpoints=0,fivestars=0,threestars=0,starpoints=0,lateshow=0,lspoints=0,sickleave=0,slpoints=0,fullattendance=2,publicity=0,ppoints=0,complaint=0,cpoints=0,nocomplaint=1,mistakelv1=0,mistakelv2=0,mistakelv3=0,mtpoints=0,nomistake=5,total=0,date=date_from,end_date=date_until)
				create.save()
			getdaily = Daily.objects.filter(date__range=(date_from,date_until))

			for get in getdaily:
				listdaily = []
				listdaily.append(get.nameone)
				listdaily.append(get.nametwo)
				listdaily.append(get.namethree)
				listdaily.append(get.namefour)
				listdaily.append(get.namefive)
				listdaily.append(get.namesix)
				listdaily.append(get.nameseven)
				listdaily.append(get.nameeight)
				listdaily.append(get.namenine)
				listdaily.append(get.nameten)
				
				if get.subject == 2.01:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('selfchecky'):
									dictdaily[i]['selfchecky'] += 1
								else:
									dictdaily[i]['selfchecky'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['selfchecky'] = 1
						else:
							pass
				elif get.subject == 1.01:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('selfcheckn'):
									dictdaily[i]['selfcheckn'] += 1
								else:
									dictdaily[i]['selfcheckn'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['selfcheckn'] = 1
						else:
							pass
				elif get.subject == 2.02:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('smileservy'):
									dictdaily[i]['smileservy'] += 1
								else:
									dictdaily[i]['smileservy'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['smileservy'] = 1
						else:
							pass
				elif get.subject == 1.02:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('smileservn'):
									dictdaily[i]['smileservn'] += 1
								else:
									dictdaily[i]['smileservn'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['smileservn'] = 1
						else:
							pass
				elif get.subject == 5.01:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('cspraiseletters'):
									dictdaily[i]['cspraiseletters'] += 1
								else:
									dictdaily[i]['cspraiseletters'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['cspraiseletters'] = 1
						else:
							pass
				elif get.subject == 5.02:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('othpraiseletters'):
									dictdaily[i]['othpraiseletters'] += 1
								else:
									dictdaily[i]['othpraiseletters'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['othpraiselettersr'] = 1
						else:
							pass
				elif get.subject == 5.03:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('fivestars'):
									dictdaily[i]['fivestars'] += 1
								else:
									dictdaily[i]['fivestars'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['fivestars'] = 1
						else:
							pass
				elif get.subject == 5.04:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('threestars'):
									dictdaily[i]['threestars'] += 1
								else:
									dictdaily[i]['threestars'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['threestars'] = 1
						else:
							pass
				elif get.subject == 5.05:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('lateshow'):
									dictdaily[i]['lateshow'] += 1
								else:
									dictdaily[i]['lateshow'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['lateshow'] = 1
						else:
							pass
				elif get.subject == 10.01:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('sickleave'):
									dictdaily[i]['sickleave'] += 1
								else:
									dictdaily[i]['sickleave'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['sickleave'] = 1
						else:
							pass
				elif get.subject == 5.06:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('publicity'):
									dictdaily[i]['publicity'] += 1
								else:
									dictdaily[i]['publicity'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['publicity'] = 1
						else:
							pass
				elif get.subject == 5.07:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('complaint'):
									dictdaily[i]['complaint'] += 1
								else:
									dictdaily[i]['complaint'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['complaint'] = 1
						else:
							pass
				elif get.subject == 2.03:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('mistakelv1'):
									dictdaily[i]['mistakelv1'] += 1
								else:
									dictdaily[i]['mistakelv1'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['mistakelv1'] = 1
						else:
							pass
				elif get.subject == 5.08:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('mistakelv2'):
									dictdaily[i]['mistakelv2'] += 1
								else:
									dictdaily[i]['mistakelv2'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['mistakelv2'] = 1
						else:
							pass
				else:
					for i in listdaily:
						if i != '无':
							if dictdaily.has_key(i):
								if dictdaily[i].has_key('mistakelv3'):
									dictdaily[i]['mistakelv3'] += 1
								else:
									dictdaily[i]['mistakelv3'] = 1
							else:
								dictdaily[i] = {}
								dictdaily[i]['mistakelv3'] = 1
						else:
							pass
			
			getranking = Ranking.objects.all()
			for key,value in dictdaily.items():
				set = Ranking.objects.get(name=key)
				if value.has_key('selfchecky'):
					set.selfchecky = value['selfchecky']
				if value.has_key('selfcheckn'):
					set.selfcheckn = value['selfcheckn']
				if value.has_key('smileservy'):
					set.smileservy = value['smileservy']
				if value.has_key('smileservn'):
					set.smileservn = value['smileservn']
				if value.has_key('cspraiseletters'):
					set.cspraiseletters = value['cspraiseletters']
				if value.has_key('othpraiseletters'):
					set.othpraiseletters = value['othpraiseletters']
				if value.has_key('fivestars'):
					set.fivestars = value['fivestars']
				if value.has_key('threestars'):
					set.threestars = value['threestars']
				if value.has_key('lateshow'):
					set.lateshow = value['lateshow']
				if value.has_key('sickleave'):
					set.sickleave = value['sickleave']
				if value.has_key('publicity'):
					set.publicity = value['publicity']
				if value.has_key('complaint'):
					set.complaint = value['complaint']
				if value.has_key('mistakelv1'):
					set.mistakelv1 = value['mistakelv1']
				if value.has_key('mistakelv2'):
					set.mistakelv2 = value['mistakelv2']
				if value.has_key('mistakelv3'):
					set.mistakelv3 = value['mistakelv3']
				set.save()
				
			for get in getranking:
				set = Ranking.objects.get(name=get.name)
				if set.skill == 0:
					set.spoints = 0
				elif set.skill == 1:
					set.spoints = 3
				elif set.skill == 2:
					set.spoints = 6
				elif set.skill == 3:
					set.spoints = 9
				elif set.skill == 4:
					set.spoints = 12
				elif set.skill == 5:
					set.spoints = 17
				elif set.skill == 6:
					set.spoints = 25
				elif set.skill == 7:
					set.spoints = 37
				elif set.skill == 8:
					set.spoints = 49
				elif set.skill == 9:
					set.spoints = 61
				else:
					set.spoints = 73
				set.scpoints = 2 * set.selfchecky - set.selfcheckn
				set.sspoints = 2 * set.smileservy - set.smileservn
				set.plpoints = 5 * set.cspraiseletters + 5 * set.othpraiseletters
				set.starpoints = 5 * set.fivestars - 5 * set.threestars
				set.lspoints = -5 * set.lateshow
				set.slpoints = -10 * set.sickleave
				if set.sickleave > 0:
					set.fullattendance = set.fullattendance - set.fullattendance
				set.ppoints = 5 * set.publicity
				set.cpoints = -5 * set.complaint
				if set.complaint > 0:
					set.nocomplaint = set.nocomplaint - set.nocomplaint
				set.mtpoints = -2 * set.mistakelv1 + (-5) * set.mistakelv2 + (-10) * set.mistakelv3
				if set.mtpoints > 0:
					set.nomistake = set.nomistake - set.nomistake
				set.total = set.eqmanage + set.assistant+ set.groupleader + set.typing + set.counting + set.accountmanage +set.courseware + set.spoints + set.scpoints + set.sspoints + set.plpoints + set.fullattendance + set.starpoints + set.lspoints + set.slpoints + set.ppoints + set.cpoints + set.nocomplaint + set.mtpoints + set.nomistake
				set.save()
			return HttpResponseRedirect('/ranking_download/')
	else:
		form = RankingForm()
	return render(req,'ranking.html',{'form':form})
	
def ranking_output(req):
	wb = xlwt.Workbook(encoding = 'utf-8')
	sheet = wb.add_sheet(u'质量评分表')
	
	font0 = xlwt.Font()
	font0.colour_index = 2
	font0.bold = True
	font0.height = 0x258
	
	alignment1 = xlwt.Alignment()
	alignment1.vert = xlwt.Alignment.VERT_CENTER
	
	font1 = xlwt.Font()
	font1.colour_index = 4
	font1.bold = True
	
	font2 = xlwt.Font()
	font2.colour_index = 2
	
	font3 = xlwt.Font()
	font3.colour_index = 3
	
	style0 = xlwt.XFStyle()
	style0.font = font0
	style0.alignment = alignment1
	
	style1 = xlwt.XFStyle()
	style1.font = font1
	
	style2 = xlwt.XFStyle()
	style2.font = font2
	
	style3 = xlwt.XFStyle()
	style3.font = font3
	
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment;filename=质量评分表.xls'
	sheet.write_merge(0,0,0,42,'质量评分表',style0)
	
	sheet.write(1,0, '姓名')
	sheet.write(1,1, '员工号')
	sheet.write(1,2, '工作号')
	sheet.write(1,3, '团队')
	sheet.write(1,4, '设备管理')
	sheet.write(1,5, '外航助理')
	sheet.write(1,6, '组长')
	sheet.write(1,7, '打字')
	sheet.write(1,8, '数票')
	sheet.write(1,9, '财务')
	sheet.write(1,10, '课件制作')
	sheet.write(1,11, '技能数',)
	sheet.write(1,12, '技能加分')
	sheet.write(1,13, '自查合格')
	sheet.write(1,14, '自查不合格')
	sheet.write(1,15, '自查得分')
	sheet.write(1,16, '微笑合格')
	sheet.write(1,17, '微笑不合格')
	sheet.write(1,18, '微笑得分')
	sheet.write(1,19, '南航表扬信')
	sheet.write(1,20, '外航表扬信')
	sheet.write(1,21, '表扬信得分')
	sheet.write(1,22, '五星')
	sheet.write(1,23, '三星')
	sheet.write(1,24, '五星得分')
	sheet.write(1,25, '迟到')
	sheet.write(1,26, '迟到扣分')
	sheet.write(1,27, '病假')
	sheet.write(1,28, '病假扣分')
	sheet.write(1,29, '全勤奖励')
	sheet.write(1,30, '宣传报道')
	sheet.write(1,31, '宣传报道得分')
	sheet.write(1,32, '投诉')
	sheet.write(1,33, '投诉扣分')
	sheet.write(1,34, '无投诉奖励')
	sheet.write(1,35, '一般差错')
	sheet.write(1,36, '中等差错')
	sheet.write(1,37, '严重差错')
	sheet.write(1,38, '差错扣分')
	sheet.write(1,39, '无差错奖励')
	sheet.write(1,40, '最终得分')
	sheet.write(1,41, '起始日期')
	sheet.write(1,42, '截止日期')
	
	row = 2
	for get in Ranking.objects.order_by('group'):
		sheet.write(row,0, get.name,style1)
		sheet.write(row,1, get.eid)
		sheet.write(row,2, get.wid)
		sheet.write(row,3, get.group)
		sheet.write(row,4, get.eqmanage)
		sheet.write(row,5, get.assistant)
		sheet.write(row,6, get.groupleader)
		sheet.write(row,7, get.typing)
		sheet.write(row,8, get.counting)
		sheet.write(row,9, get.accountmanage)
		sheet.write(row,10, get.courseware)
		sheet.write(row,11, get.skill)
		sheet.write(row,12, get.spoints,style2)
		sheet.write(row,13, get.selfchecky)
		sheet.write(row,14, get.selfcheckn)
		sheet.write(row,15, get.scpoints,style2)
		sheet.write(row,16, get.smileservy)
		sheet.write(row,17, get.smileservn)
		sheet.write(row,18, get.sspoints,style2)
		sheet.write(row,19, get.cspraiseletters)
		sheet.write(row,20, get.othpraiseletters)
		sheet.write(row,21, get.plpoints,style2)
		sheet.write(row,22, get.fivestars)
		sheet.write(row,23, get.threestars)
		sheet.write(row,24, get.starpoints,style2)
		sheet.write(row,25, get.lateshow)
		sheet.write(row,26, get.lspoints,style3)
		sheet.write(row,27, get.sickleave)
		sheet.write(row,28, get.slpoints,style3)
		sheet.write(row,29, get.fullattendance)
		sheet.write(row,30, get.publicity)
		sheet.write(row,31, get.ppoints)
		sheet.write(row,32, get.complaint,style2)
		sheet.write(row,33, get.cpoints,style3)
		sheet.write(row,34, get.nocomplaint)
		sheet.write(row,35, get.mistakelv1)
		sheet.write(row,36, get.mistakelv2)
		sheet.write(row,37, get.mistakelv3)
		sheet.write(row,38, get.mtpoints,style3)
		sheet.write(row,39, get.nomistake)
		sheet.write(row,40, get.total)
		sheet.write(row,41, str(get.date))
		sheet.write(row,42, str(get.end_date))
		row = row + 1

	output = StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response
	
def success(req):
	return render(req,'success.html')