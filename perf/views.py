# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from perf.models import Add,Count
from perf.forms import AddForm,CountForm,VerifyForm
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
	if req.method == 'POST':
		form = AddForm(req.POST)
		if form.is_valid():
			perf_num=form.cleaned_data['performance']
			values_num=form.cleaned_data['values']
			new_perf=form.save(commit=False)
			if perf_num == 5.0:
				if values_num > 20:
					new_perf.workload = 25
				elif values_num > 15:
					new_perf.workload = 20
				elif values_num > 10:
					new_perf.workload = 15
				elif values_num > 5:
					new_perf.workload = 10
				else:
					new_perf.workload = 5
			elif perf_num == 20.0:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 20.1:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 20.2:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 20.3:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 20.4:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 10.0:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 10.1:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 15.0:
				new_perf.workload = int(perf_num)*values_num
			elif perf_num == 1.0:
				new_perf.point = int(perf_num)*values_num
			elif perf_num == 1.1:
				new_perf.point = int(perf_num)*values_num
			elif perf_num == 1.2:
				new_perf.point = int(perf_num)*values_num
			else:
				new_perf.point = int(perf_num)*values_num
			new_perf.save()
			form.save_m2m()
			return HttpResponseRedirect('/success/')
	else:
		form = AddForm()
	return render(req,'add.html',{'form':form})

def excel_output(req):
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

def count(req):
	if req.method == 'POST':
		form = CountForm(req.POST)
		if form.is_valid():
			Count.objects.all().delete()
			date_from = form.cleaned_data['start_date']
			date_until = form.cleaned_data['end_date']
			sets = Add.objects.filter(date__range=(date_from,date_until),verify = '已审核')
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