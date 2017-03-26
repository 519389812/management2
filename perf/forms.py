# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from perf.models import Add,Addother
from django.db import models

class AddForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Add
		fields = ('name','performance','values','performancetwo','valuestwo','performancethree','valuesthree','supervisor','date','comment')

class AddotherForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Addother
		fields = ('other_name','airline','taskclass','taskone','tasktwo','taskthree','taskfour','taskfive','task_values','other_date')
