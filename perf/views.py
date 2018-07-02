# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from perf.models import Add,Addother
from perf.forms import AddForm,AddotherForm
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
				elif values_num > 0:
					workload_one = 5
				else:
					pass
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
			elif perf_num == 30.1:
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
				elif values_numtwo > 0:
					workload_two = 5
				else:
					pass
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
			elif perf_numtwo == 30.1:
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
				elif values_numthree > 0:
					workload_three = 5
				else:
					pass
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
			elif perf_numthree == 30.1:
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
				elif taskfiveval_num > 0:
					workload_taskfive = 5
				else:
					pass
			elif taskfive_num == 15.002:
				workload_taskfive = round(taskfive_num,1) * taskfiveval_num
			elif taskfive_num == 0.0:
				workload_taskfive = 0
			elif taskfive_num == 0.502:
				if taskfiveval_num < 0.5:
					other_perf.other_point = 0.5
				else:
					if other_perf.airline == 252.0001:
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 3 * 110.88
					else:
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 2.5 * other_perf.airline * 1.1
			elif taskfive_num == 0.503:
				if other_perf.airline == 252.0001:
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
					if other_perf.airline == 252.0001:
						other_perf.taskclass = 0.0
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 3 * 110.88
					else:
						other_perf.taskclass = 0.0
						other_perf.other_point = 0.5
						workload_taskfive = taskfiveval_num / 2.5 * other_perf.airline * 1.1							
			if other_perf.airline == 252.0001:
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

def welcome(req):
	return render(req,'welcome1.html')
	
def success(req):
	return render(req,'success1.html')
	
def aboutus(req):
	return render(req,'aboutus.html')
	
def contact(req):
	return render(req,'contact.html')
	
def addcheck(request):
	return render(request, 'add.html')

def addothercheck(request):
	return render(request, 'addother.html')
	
def validate(request):
	name = request.GET['name']
	namelist = []
	allname = Staff.objects.all()
	for get in allname:
		namelist.append(get.name)
	if name in namelist:
		return HttpResponse('输入正确！')
	elif name == '无':
		return HttpResponse('')
	else:
		return HttpResponse('姓名错误或未录入档案！')