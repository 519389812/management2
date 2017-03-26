# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from staff.models import Staff
from staff.forms import StaffForm
from administrator.models import Daily
from administrator.forms import DailyForm
import sqlite3
import sys
#from __future__ import unicode_literals
from django.http import JsonResponse
import xlwt
from cStringIO import StringIO
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime
from collections import Counter
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def daily(req):
	if req.method == 'POST':
		form = DailyForm(req.POST)
		if form.is_valid():
			#nameone = form.cleaned_data['nameone']
			daily = form.save()
			return HttpResponseRedirect('/success/')
	else:
		form = DailyForm()
	return render(req,'daily1.html',{'form':form})

    
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
