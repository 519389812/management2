# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from perf.models import Add,Count,Addother,Countother
from django.db import models

class AddForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Add
		fields = ('name','team','performance','values','performancetwo','valuestwo','performancethree','valuesthree','supervisor','date','comment')

class AddotherForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Addother
		fields = ('other_name','other_team','airline','taskclass','taskone','tasktwo','taskthree','taskfour','other_date')
		
class CountForm(ModelForm):
	#year = forms.integerField(disabled=True,required=False)
	#month = forms.integerField(disabled=True)

	class Meta:
		model = Count
		fields = ('team','start_date','end_date')

class CountotherForm(ModelForm):
	#year = forms.integerField(disabled=True,required=False)
	#month = forms.integerField(disabled=True)

	class Meta:
		model = Countother
		fields = ('other_team','start_date','end_date')
		
class VerifyForm(ModelForm):
	#workload = forms.FloatField(disabled=True,required=False)
	#verify = forms.BooleanField(disabled=True)

	class Meta:
		model = Add
		fields = ('verify',)