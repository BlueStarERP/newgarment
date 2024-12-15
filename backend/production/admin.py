from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(LineSchedule)
admin.site.register(LineName)
admin.site.register(LineInputAcc)
admin.site.register(DailyLineHandover)