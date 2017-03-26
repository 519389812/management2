"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from perf import views as p_views
from administrator import views as a_views
from report import views as r_views
#from staff import views
import xadmin
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()
from django.conf import settings


urlpatterns = [
	url(r'^add/$',p_views.add,name='add'),
	url(r'^addother/$',p_views.addother,name='addother'),
	url(r'^$',p_views.welcome,name='welcome'),
	url(r'^admin', admin.site.urls),
	url(r'^481/', xadmin.site.urls,name='481'),
	url(r'^excel_download/$',r_views.count_output,name='cz_output'),
	url(r'^other_download/$',r_views.other_output,name='other_output'),
	url(r'^count/$',r_views.count,name='count'),
	url(r'^countother/$',r_views.countother,name='countother'),
#	url(r'^verify/$',views.verify),
	url(r'^success/$',p_views.success,name='success'),
	url(r'^daily/$',a_views.daily,name='daily'),
	url(r'^ranking/$',r_views.ranking,name='ranking'),
	url(r'^ranking_download/$',r_views.ranking_output,name='ranking_output'),
	
	url(r'^validate/$', a_views.validate, name='validate'),
	url(r'^aboutus', p_views.aboutus, name='aboutus'),
	url(r'^contact/$', p_views.contact, name='contact'),
]