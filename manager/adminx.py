# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from manager.models import IDC, Host, MaintainLog, HostGroup, AccessRecord
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from datalib.models import Datalib
from perf.models import Add,Addother
from staff.models import Staff
from administrator.models import Daily
from report.models import Ranking
import django.utils.timezone as timezone
from django.contrib import admin
from django.http import HttpResponse,HttpResponseRedirect
import copy
from django import forms
from django.db import models
from django.core.exceptions import PermissionDenied
from django.forms.models import modelform_factory
from django.template.response import TemplateResponse
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _, ugettext_lazy
from xadmin.layout import FormHelper, Layout, Fieldset, Container, Col
from xadmin.plugins.actions import BaseActionView, ACTION_CHECKBOX_NAME
from xadmin.util import model_ngettext, vendor
from xadmin.views.base import filter_hook
from xadmin.views.edit import ModelFormAdminView

class MyChangeVerifyAction(BaseActionView):
	action_name = 'my_action1'
	description = _(u'Test selected 批量设置已审核')
	model_perm = 'change'
	def do_action(self, queryset):
		for obj in queryset:
			obj.verify = '已审核'
			obj.save()
#		return HttpResponse('设置成功')

class MyChangeUnverifyAction(BaseActionView):
	action_name = 'my_action2'
	description = _(u'Test selected 批量设置未通过')
	model_perm = 'change'
	def do_action(self, queryset):
		for obj in queryset:
			obj.verify = '未通过'
			obj.save()
#		return HttpResponse('设置成功')

class MyChangeOtherVerifyAction(BaseActionView):
	action_name = 'my_action3'
	description = _(u'Test selected 批量设置已审核')
	model_perm = 'change'
	def do_action(self, queryset):
		for obj in queryset:
			obj.other_verify = '已审核'
			obj.save()
#		return HttpResponse('设置成功')

class MyChangeOtherUnverifyAction(BaseActionView):
	action_name = 'my_action4'
	description = _(u'Test selected 批量设置未通过')
	model_perm = 'change'
	def do_action(self, queryset):
		for obj in queryset:
			obj.other_verify = '未通过'
			obj.save()
#		return HttpResponse('设置成功')

class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "欢迎！", "content": "<h3> 欢迎使用工作量自助登记系统! </h3><p>欢迎反馈您宝贵的意见和建议<br/>管理员:<br/>刘偲翀:15626293425<br/>梁良:18611282168</p>"},
            #{"type": "chart", "model": "manager.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2013-01-08', 'p': 1, '_p_date__lt': '2013-01-29'}},
            #{"type": "list", "model": "manager.host", 'params': {
            #    'o':'-guarantee_date'}},
        ],
        [
            {"type": "qbutton", "title": "快速访问", "btns":  [{"model": "staff.Staff", "title": "员工档案"},{"model": "perf.Add", "title": "CZ绩效审核"}, {"model": "perf.Addother", "title": "外航绩效审核"},{"model": "administrator.Daily", "title": "检查明细"}, {"url": "https://checkinlib.heroku.com/count", "title": "绩效统计下载"}, {"url": "https://checkinlib.heroku.com/countother", "title": "外航统计下载"},{"url": "https://checkinlib.heroku.com/ranking", "title": "导出质量评分表"}]},
            #{"type": "addform", "model": MaintainLog},
        ]
    ]
xadmin.sites.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.sites.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    global_search_models = [Host, IDC]
    global_models_icon = {
        Host: 'fa fa-laptop', IDC: 'fa fa-cloud'
    }
    menu_style = 'default'#'accordion'
	
    site_title = 'Check-in Lib'  #设置base_site.html的Title
    site_footer = 'Check-in Lib 1.2 server since 2016-11-8'  #设置base_site.html的Footer
	
	
xadmin.sites.site.register(views.CommAdminView, GlobalSetting)


class MaintainInline(object):
    model = MaintainLog
    extra = 1
    style = 'accordion'


class IDCAdmin(object):
    list_display = ('name', 'description', 'create_time')
    list_display_links = ('name',)
    wizard_form_list = [
        ('First\'s Form', ('name', 'description')),
        ('Second Form', ('contact', 'telphone', 'address')),
        ('Thread Form', ('customer_id',))
    ]

    search_fields = ['name']
    relfield_style = 'fk-select'
    reversion_enable = True

    actions = [BatchChangeAction, ]
    batch_fields = ('contact', 'groups')


class HostAdmin(object):
    def open_web(self, instance):
        return "<a href='http://%s' target='_blank'>Open</a>" % instance.ip
    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True

    list_display = ('name', 'idc', 'guarantee_date', 'service_type',
                    'status', 'open_web', 'description')
    list_display_links = ('name',)

    raw_id_fields = ('idc',)
    style_fields = {'system': "radio-inline"}

    search_fields = ['name', 'ip', 'description']
    list_filter = ['idc', 'guarantee_date', 'status', 'brand', 'model',
                   'cpu', 'core_num', 'hard_disk', 'memory', ('service_type',xadmin.filters.MultiSelectFieldListFilter)]
    
    list_quick_filter = ['service_type',{'field':'idc__name','limit':10}]
    list_bookmarks = [{'title': "Need Guarantee", 'query': {'status__exact': 2}, 'order': ('-guarantee_date',), 'cols': ('brand', 'guarantee_date', 'service_type')}]

    show_detail_fields = ('idc',)
    list_editable = (
        'name', 'idc', 'guarantee_date', 'service_type', 'description')
    save_as = True

    aggregate_fields = {"guarantee_date": "min"}
    grid_layouts = ('table', 'thumbnails')

    form_layout = (
        Main(
            TabHolder(
                Tab('Comm Fields',
                    Fieldset('Company data',
                             'name', 'idc',
                             description="some comm fields, required"
                             ),
                    Inline(MaintainLog),
                    ),
                Tab('Extend Fields',
                    Fieldset('Contact details',
                             'service_type',
                             Row('brand', 'model'),
                             Row('cpu', 'core_num'),
                             Row(AppendedText(
                                 'hard_disk', 'G'), AppendedText('memory', "G")),
                             'guarantee_date'
                             ),
                    ),
            ),
        ),
        Side(
            Fieldset('Status data',
                     'status', 'ssh_port', 'ip'
                     ),
        )
    )
    inlines = [MaintainInline]
    reversion_enable = True
    
    data_charts = {
        "host_service_type_counts": {'title': u"Host service type count", "x-field": "service_type", "y-field": ("service_type",), 
                              "option": {
                                         "series": {"bars": {"align": "center", "barWidth": 0.8,'show':True}}, 
                                         "xaxis": {"aggregate": "count", "mode": "categories"},
                                         },
                              },
    }
    
class HostGroupAdmin(object):
    list_display = ('name', 'description')
    list_display_links = ('name',)

    search_fields = ['name']
    style_fields = {'hosts': 'checkbox-inline'}


class MaintainLogAdmin(object):
    list_display = (
        'host', 'maintain_type', 'hard_type', 'time', 'operator', 'note')
    list_display_links = ('host',)

    list_filter = ['host', 'maintain_type', 'hard_type', 'time', 'operator']
    search_fields = ['note']

    form_layout = (
        Col("col2",
            Fieldset('Record data',
                     'time', 'note',
                     css_class='unsort short_label no_title'
                     ),
            span=9, horizontal=True
            ),
        Col("col1",
            Fieldset('Comm data',
                     'host', 'maintain_type'
                     ),
            Fieldset('Maintain details',
                     'hard_type', 'operator'
                     ),
            span=3
            )
    )
    reversion_enable = True


class AccessRecordAdmin(object):
    def avg_count(self, instance):
        return int(instance.view_count / instance.user_count)
    avg_count.short_description = "Avg Count"
    avg_count.allow_tags = True
    avg_count.is_column = True

    list_display = ('date', 'user_count', 'view_count', 'avg_count')
    list_display_links = ('date',)

    list_filter = ['date', 'user_count', 'view_count']
    actions = None
    aggregate_fields = {"user_count": "sum", 'view_count': "sum"}

    refresh_times = (3, 5, 10)
    data_charts = {
        "user_count": {'title': u"User Report", "x-field": "date", "y-field": ("user_count", "view_count"), "order": ('date',)},
        "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)},
        "per_month": {'title': u"Monthly Users", "x-field": "_chart_month", "y-field": ("user_count", ), 
                              "option": {
                                         "series": {"bars": {"align": "center", "barWidth": 0.8,'show':True}}, 
                                         "xaxis": {"aggregate": "sum", "mode": "categories"},
                                         },
                            },
    }
    
    def _chart_month(self,obj):
        return obj.date.strftime("%B")
        

xadmin.sites.site.register(Host, HostAdmin)
xadmin.sites.site.register(HostGroup, HostGroupAdmin)
xadmin.sites.site.register(MaintainLog, MaintainLogAdmin)
xadmin.sites.site.register(IDC, IDCAdmin)
xadmin.sites.site.register(AccessRecord, AccessRecordAdmin)

class DatalibAdmin(object):
	list_display = ('case_id','case_title','case_type','destination','direct_liability','date')
	list_display_links = ('case_id',)
	list_filter = ('case_title', 'case_type','destination','direct_liability', 'date')
	#list_editable = ['case_type', ]
	search_fields = ('case_title','case_type','destination','direct_liability','date')
	show_detail_fields = ('case_title',)
xadmin.sites.site.register(Datalib, DatalibAdmin)

class AddAdmin(object):
	list_display = ('perf_id','name', 'team','performance','values','performancetwo','valuestwo','performancethree','valuesthree','workload','point','supervisor','date','verify','comment')
	list_display_links = ('perf_id',)
	list_filter = ('name','team','supervisor','date','verify')
	list_editable = ['verify', ]
	search_fields = ('name', 'team', 'supervisor', 'date', )
	show_detail_fields = ('perf_id',)
	readonly_fields = ['verify_auth', 'verify_date']
	actions = [MyChangeVerifyAction,MyChangeUnverifyAction, ]
xadmin.site.register(Add, AddAdmin)

class AddotherAdmin(object):
	list_display = ('other_id','other_name','other_team','airline','taskclass','taskone','tasktwo','taskthree','taskfour','taskfive','task_values','other_workload','other_point','other_date','other_verify')
	list_display_links = ('other_id',)
	list_filter = ('other_name','airline','other_team','other_date','other_verify')
	list_editable = ['other_verify', ]
	search_fields = ('other_name', 'other_team', 'other_date', )
	show_detail_fields = ('other_id',)
	readonly_fields = ['other_auth', 'other_verifydate']
	actions = [MyChangeOtherVerifyAction,MyChangeOtherUnverifyAction, ]
xadmin.site.register(Addother, AddotherAdmin)

class DailyAdmin(object):
	list_display = ('id','date','subject','airlinecode','nameone','nametwo','namethree','namefour','namefive','namesix','nameseven','nameeight','namenine','nameten')
	list_display_links = ('id',)
	list_filter = ('date','subject','airlinecode','nameone','nametwo','namethree','namefour','namefive','namesix','nameseven','nameeight','namenine','nameten')
	list_editable = ['date','subject','airlinecode', ]
	search_fields = ('date','subject','airlinecode', )
	show_detail_fields = ('id',)
#	readonly_fields = ['other_auth', 'other_verifydate']
#	actions = [MyChangeOtherVerifyAction,MyChangeOtherUnverifyAction, ]
xadmin.site.register(Daily, DailyAdmin)

class StaffAdmin(object):
	list_display = ('id','name','eid','wid','group','birth','eqmanage','assistant','groupleader','typing','counting','accountmanage','courseware','af','br','ci','jl','ka','ke','mh','oz','su','sq','tg','vn','status')
	list_display_links = ('id',)
	list_filter = ('name','eid','wid','group','birth','eqmanage','assistant','groupleader','typing','counting','accountmanage','courseware','af','br','ci','jl','ka','ke','mh','oz','su','sq','tg','vn','status')
	list_editable = ['name','eid','wid','group','birth','eqmanage','assistant','groupleader','typing','counting','accountmanage','courseware','af','br','ci','jl','ka','ke','mh','oz','su','sq','tg','vn','status', ]
	search_fields = ('name','eid','wid','group','birth','eqmanage','assistant','groupleader','typing','counting','accountmanage','courseware','af','br','ci','jl','ka','ke','mh','oz','su','sq','tg','vn','status')
	show_detail_fields = ('id',)
#	readonly_fields = ['other_auth', 'other_verifydate']
#	actions = [MyChangeOtherVerifyAction,MyChangeOtherUnverifyAction, ]
xadmin.site.register(Staff, StaffAdmin)