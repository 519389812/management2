# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from administrator.models import Daily
from django.db import models
		
class DailyForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Daily
		fields = ('date','subject','airlinecode','nameone','nametwo','namethree','namefour','namefive','namesix','nameseven','nameeight','namenine','nameten')
		