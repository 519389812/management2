# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from perf.models import Add,Count,Addother,Countother
from perf.forms import AddForm,CountForm,AddotherForm,CountotherForm
import sqlite3
import sys
#from __future__ import unicode_literals
from django.http import JsonResponse
import xlwt
from cStringIO import StringIO
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime


# Create your views here.
def add(req):
	workload_one = 0
	workload_two = 0
	workload_three = 0
	point_one = 0
	point_two = 0
	point_three = 0
	if req.method == 'POST':
		form = AddForm(req.POST)
		if form.is_valid():
			perf_num=form.cleaned_data['performance']
			values_num=form.cleaned_data['values']
			perf_numtwo=form.cleaned_data['performancetwo']
			values_numtwo=form.cleaned_data['valuestwo']
			perf_numthree=form.cleaned_data['performancethree']
			values_numthree=form.cleaned_data['valuesthree']
			new_perf=form.save(commit=False)
			if perf_num == 5.0:      #first round
				if values_num > 20:
					workload_one = 25
				elif values_num > 15:
					workload_one = 20
				elif values_num > 10:
					workload_one = 15
				elif values_num > 5:
					workload_one = 10
				else:
					workload_one = 5
			elif perf_num == 0.0:
				workload_one = 0
			elif perf_num == 20.0:
				workload_one = int(perf_num)*values_num
			elif perf_num == 20.1:
				workload_one = int(perf_num)*values_num
			elif perf_num == 20.2:
				workload_one = int(perf_num)*values_num
			elif perf_num == 20.3:
				workload_one = int(perf_num)*values_num
			elif perf_num == 20.4:
				workload_one = int(perf_num)*values_num
			elif perf_num == 10.0:
				workload_one = int(perf_num)*values_num
			elif perf_num == 10.1:
				workload_one = int(perf_num)*values_num
			elif perf_num == 15.0:
				workload_one = int(perf_num)*values_num
			else:
				point_one = int(perf_num)*values_num
			if perf_numtwo == 5.0:       #secend round
				if values_numtwo > 20:
					workload_two = 25
				elif values_numtwo > 15:
					workload_two = 20
				elif values_numtwo > 10:
					workload_two = 15
				elif values_numtwo > 5:
					workload_two = 10
				else:
					workload_two = 5
			elif perf_numtwo == 0.0:
				workload_two = 0
			elif perf_numtwo == 20.0:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 20.1:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 20.2:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 20.3:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 20.4:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 10.0:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 10.1:
				workload_two = int(perf_numtwo)*values_numtwo
			elif perf_numtwo == 15.0:
				workload_two = int(perf_numtwo)*values_numtwo
			else:
				point_two = int(perf_numtwo)*values_numtwo
			if perf_numthree == 5.0:       #third round
				if values_numthree > 20:
					workload_three = 25
				elif values_numthree > 15:
					workload_three = 20
				elif values_numthree > 10:
					workload_three = 15
				elif values_numthree > 5:
					workload_three = 10
				else:
					workload_three = 5
			elif perf_numthree == 0.0:
				workload_three = 0
			elif perf_numthree == 20.0:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 20.1:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 20.2:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 20.3:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 20.4:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 10.0:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 10.1:
				workload_three = int(perf_numthree)*values_numthree
			elif perf_numthree == 15.0:
				workload_three = int(perf_numthree)*values_numthree
			else:
				point_three = int(perf_numthree)*values_numthree
			new_perf.workload = workload_one + workload_two + workload_three
			new_perf.point = point_one + point_two + point_three
			new_perf.save()
			form.save_m2m()
			return HttpResponseRedirect('/success/')
	else:
		form = AddForm()
	return render(req,'add.html',{'form':form})

#------------------------------------------------------------------------------#

def addother(req):
	workload_taskfive = 0
	point_taskfive = 0
	if req.method == 'POST':
		form = AddotherForm(req.POST)
		if form.is_valid():
			taskfive_num=form.cleaned_data['taskfive']
			taskfiveval_num=form.cleaned_data['task_values']
			other_perf=form.save(commit=False)
			if taskfive_num == 5.001:
				if taskfiveval_num > 20:
					workload_taskfive = 25
				elif taskfiveval_num > 15:
					workload_taskfive = 20
				elif taskfiveval_num > 10:
					workload_taskfive = 15
				elif taskfiveval_num > 5:
					workload_taskfive = 10
				else:
					workload_taskfive = 5
			elif taskfive_num == 15.002:
				workload_taskfive = round(taskfive_num,1) * taskfiveval_num
			elif taskfive_num == 0.0:
				workload_taskfive = 0
			elif taskfive_num == 0.502:
				if taskfiveval_num < 0.5:
					other_perf.other_point = 0.5
				else:
					if other_perf.airline == 252.001:
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 3 * 110.88
					else:
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 2.5 * other_perf.airline * 1.1
			elif taskfive_num == 0.503:
				if other_perf.airline == 252.001:
					other_perf.taskclass = 0.0
					other_perf.other_point = 0.5
					other_perf.task_values = 1.0
					workload_taskfive = 252
				else:
					other_perf.taskclass = 0.0
					other_perf.other_point = 0.5
					other_perf.task_values = 1.0
					workload_taskfive = 1.3 * other_perf.airline
			elif taskfive_num == 0.504:
				other_perf.taskclass = 0.0
				other_perf.other_point = 0.5
				other_perf.task_values = 1.0
			else:
				if taskfiveval_num < 0.5:
					other_perf.taskclass = 0.0
					other_perf.other_point = 0.5
				else:
					if other_perf.airline == 252.001:
						other_perf.taskclass = 0.0
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 3 * 110.88
					else:
						other_perf.taskclass = 0.0
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 2.5 * other_perf.airline * 1.1							
			if other_perf.airline == 252.001:
				if other_perf.taskclass == 0.0:
					other_perf.other_workload = round(other_perf.taskone,1) + round(other_perf.tasktwo,1) + round(other_perf.taskthree,1) + round(other_perf.taskfour,1) + round(workload_taskfive,2)
				elif other_perf.taskclass == 1.3:
					other_perf.other_workload = 252 + round(other_perf.taskone,1) + round(other_perf.tasktwo,1) + round(other_perf.taskthree,1) + round(other_perf.taskfour,1) + round(workload_taskfive,2)
				elif other_perf.taskclass == 1.2:
					other_perf.other_workload = 120.96 + round(other_perf.taskone,1) + round(other_perf.tasktwo,1) + round(other_perf.taskthree,1) + round(other_perf.taskfour,1) + round(workload_taskfive,2)
				else:
					other_perf.other_workload = 110.88 + round(other_perf.taskone,1) + round(other_perf.tasktwo,1) + round(other_perf.taskthree,1) + round(other_perf.taskfour,1) + round(workload_taskfive,2)
			else:
				other_perf.other_workload = round(other_perf.airline,1) * round(other_perf.taskclass,1) + round(other_perf.taskone,1) + round(other_perf.tasktwo,1) + round(other_perf.taskthree,1) + round(other_perf.taskfour,1) + round(workload_taskfive,2)
			other_perf.save()
			form.save_m2m()
			return HttpResponseRedirect('/success/')
	else:
		form = AddotherForm()
	return render(req,'add4.html',{'form':form})

def count_output(req):
	wb = xlwt.Workbook(encoding = 'utf-8')
	sheet = wb.add_sheet(u'统计')
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment;filename=myperf.xls'
	sheet.write(0,0, '姓名')
	sheet.write(0,1, '室别')
	sheet.write(0,2, '起始日期')
	sheet.write(0,3, '截止日期')
	sheet.write(0,4, '工作量')
	sheet.write(0,5, '绩效加分')
	
	row = 1
	for count in Count.objects.all():
		sheet.write(row,0, count.name)
		sheet.write(row,1, count.team)
		sheet.write(row,2, str(count.start_date))
		sheet.write(row,3, str(count.end_date))
		sheet.write(row,4, count.workload)
		sheet.write(row,5, count.point)
		row = row + 1

	output = StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response

#-----------------------------------------------------------------------------------------------------------#

def other_output(req):
	wb = xlwt.Workbook(encoding = 'utf-8')
	sheet = wb.add_sheet(u'统计')
	response = HttpResponse(content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment;filename=myotherperf.xls'
	sheet.write(0,0, '姓名')
	sheet.write(0,1, '室别')
	sheet.write(0,2, '起始日期')
	sheet.write(0,3, '截止日期')
	sheet.write(0,4, '工作量')
	sheet.write(0,5, '加分')
	
	row = 1
	for countother in Countother.objects.all():
		sheet.write(row,0, countother.other_name)
		sheet.write(row,1, countother.other_team)
		sheet.write(row,2, str(countother.start_date))
		sheet.write(row,3, str(countother.end_date))
		sheet.write(row,4, countother.other_workload)
		sheet.write(row,5, countother.other_point)
		row = row + 1

	output = StringIO()
	wb.save(output)
	output.seek(0)
	response.write(output.getvalue())
	return response

def count(req):
	if req.method == 'POST':
		form = CountForm(req.POST)
		if form.is_valid():
			Count.objects.all().delete()
			teamchoice = form.cleaned_data['team']
			date_from = form.cleaned_data['start_date']
			date_until = form.cleaned_data['end_date']
			if teamchoice == '全部':
				sets = Add.objects.filter(date__range=(date_from,date_until),verify = '已审核')
			else:
				sets = Add.objects.filter(date__range=(date_from,date_until),verify = '已审核',team = teamchoice)
			for set in sets:
				if len(Count.objects.filter(name = set.name))>0:
					get = Count.objects.get(name = set.name)
					get.workload = get.workload + set.workload
					get.point = get.point + set.point
					get.save()
				else:
					create = Count(name=set.name,team=set.team,workload=set.workload,point=set.point,start_date=date_from,end_date=date_until)
					create.save()
			return HttpResponseRedirect('/excel_download/')
	else:
		form = CountForm()
	return render(req,'count.html',{'form':form})

#-----------------------------------------------------------------------------------------------------------------------#

def countother(req):
	if req.method == 'POST':
		form = CountotherForm(req.POST)
		if form.is_valid():
			Countother.objects.all().delete()
			teamchoice = form.cleaned_data['other_team']
			date_from = form.cleaned_data['start_date']
			date_until = form.cleaned_data['end_date']
			if teamchoice == '全部':
				sets = Addother.objects.filter(other_date__range=(date_from,date_until),other_verify = '已审核')
			else:
				sets = Addother.objects.filter(other_date__range=(date_from,date_until),other_verify = '已审核',other_team = teamchoice)
			for set in sets:
				if len(Countother.objects.filter(other_name = set.other_name))>0:
					get = Countother.objects.get(other_name = set.other_name)
					get.other_workload = get.other_workload + set.other_workload
					get.other_point = get.other_point + set.other_point
					get.save()
				else:
					create = Countother(other_name=set.other_name,other_team=set.other_team,other_workload=set.other_workload,other_point=set.other_point,start_date=date_from,end_date=date_until)
					create.save()
			return HttpResponseRedirect('/other_download/')
	else:
		form = CountotherForm()
	return render(req,'countother.html',{'form':form})

def verify(req):
	details = Add.objects.filter(verify='等待审核')
	list_detail = list()
	for detail in details:
		list_detail.append(str(detail.name))
		#dict_detail = {'姓名':detail.name,'室别':detail.team,'绩效类型':detail.performance,'绩效量':detail.values,'日期':str(detail.date)}
	return JsonResponse(list_detail,safe=False)

def welcome(req):
	return render(req,'welcome.html')
	
def success(req):
	return render(req,'success.html')