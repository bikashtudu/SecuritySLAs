from django.contrib import admin
from .models import VMs
from .models import UserVMs
from .models import SLAStatus

# Register your models here.

admin.site.register(VMs)
admin.site.register(UserVMs)
admin.site.register(SLAStatus)
