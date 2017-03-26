# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from report.models import Count,Countother,Ranking
from django.db import models
		
class CountForm(ModelForm):
	#year = forms.integerField(disabled=True,required=False)
	#month = forms.integerField(disabled=True)

	class Meta:
		model = Count
		fields = ('start_date','end_date')

class CountotherForm(ModelForm):
	#year = forms.integerField(disabled=True,required=False)
	#month = forms.integerField(disabled=True)

	class Meta:
		model = Countother
		fields = ('start_date','end_date')

class RankingForm(ModelForm):
	#year = forms.integerField(disabled=True,required=False)
	#month = forms.integerField(disabled=True)

	class Meta:
		model = Ranking
		fields = ('date','end_date',)