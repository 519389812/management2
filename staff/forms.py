# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from staff.models import Staff
from django.db import models

class StaffForm(ModelForm):
	#verify_date = forms.DateTimeField(required=False)
	#verify_auth = forms.CharField(required=False)

	class Meta:
		model = Staff
		fields = ('name','eid','wid','group','eqmanage','assistant','groupleader','typing','counting','accountmanage','courseware','af','br','ci','jl','ka','ke','mh','oz','su','sq','tg','vn','status')