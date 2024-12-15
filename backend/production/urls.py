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
    path('LineinputFabric/', LineinputFabric.as_view(), name='LineinputFabric'),

# Sewing 
    path('DailyLineDashboard/', DailyLineDashboard.as_view(), name='DailyLineDashboard'),
    path('EntryLineHandover/<int:id>', EntryLineHandover.as_view(), name='EntryLineHandover'),
    path('SewingOperatorGroup/<int:id>', SewingOperatorGroup.as_view(), name='SewingOperatorGroup'),
    path('SewingOptCMP/<int:id>', SewingOptCMP.as_view(), name='SewingOptCMP'),

# cutting
    path('CuttingView/', CuttingView.as_view(), name='CuttingView'),
    path('CuttingRequestByLine/<int:id>', CuttingRequestByLine.as_view(), name='CuttingRequestByLine'),
]