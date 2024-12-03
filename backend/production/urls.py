from django.urls import path
from .views import *
from . import views
app_name = 'production'
urlpatterns = [
    path('ScheduleView/', ScheduleView.as_view(), name='ScheduleView'),
    path('ScheduleByLine/<int:id>/', ScheduleByLine.as_view(), name='ScheduleByLine'),
    path('ScheduleData/<int:id>', ScheduleData.as_view(), name='ScheduleData'),
    path('ScheduleDetail/<int:id>/', ScheduleDetail.as_view(), name='ScheduleDetail'),
    path('ProductionLineList/', ProductionLineList.as_view(), name='ProductionLineList'),
    path('LineinputAcc/', LineinputAcc.as_view(), name='LineinputAcc'),
]