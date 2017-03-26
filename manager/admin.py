from django.contrib import admin
import xadmin
from manager.models import IDC, Host, MaintainLog, HostGroup, AccessRecord
from perf.models import Add,Addother
from datalib.models import Datalib

# Register your models here.
admin.site.register(Add)
#admin.site.register(Datalib)
admin.site.register(Addother)
#admin.site.register(Count)
#admin.site.register(Countother)
#admin.site.register(IDC)
#admin.site.register(Host)
#admin.site.register(MaintainLog)
#admin.site.register(HostGroup)
#admin.site.register(AccessRecord)

#xadmin.site.register(Add)
#xadmin.site.register(Datalib)
#admin.site.register(Addother)
#admin.site.register(Count)
#admin.site.register(Countother)
#xadmin.site.register(IDC)
#xadmin.site.register(Host)
#xadmin.site.register(MaintainLog)
#xadmin.site.register(HostGroup)
#xadmin.site.register(AccessRecord)

