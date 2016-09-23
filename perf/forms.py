# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from perf.models import Add,Count
from django.db import models

class AddForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Add
		fields = ('name','team','performance','values','date','comment')
		
class CountForm(ModelForm):
	#year = forms.integerField(disabled=True,required=False)
	#month = forms.integerField(disabled=True)

	class Meta:
		model = Count
		fields = ('year','month')
		
class VerifyForm(ModelForm):
	#workload = forms.FloatField(disabled=True,required=False)
	#verify = forms.BooleanField(disabled=True)

	class Meta:
		model = Add
		fields = ('verify',)