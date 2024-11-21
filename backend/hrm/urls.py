from django.urls import path
from .views import *
from . import views
app_name = 'hrm'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('departmentview/', departmentview.as_view(), name='departmentview'),
    path('department_delete/<int:id>/', department_delete.as_view(), name='department_delete'),

    path('positionview/', positionview.as_view(), name='positionview'),
    path('employeeview/', employeeview.as_view(), name='employeeview'),
    path('createemployee/', createemployee.as_view(), name='createemployee'),

    
    path('EmpCreate/', EmpCreate.as_view(), name='EmpCreate'),
    path('EmployeeDetailView/<int:pk>/', EmployeeDetailView.as_view(), name='EmployeeDetailView'),
    path('EmpUpdate/<int:pk>/', EmpUpdate.as_view(), name='EmpUpdate'),

    path('delete_image/<int:pk>/', views.delete_image, name='delete_image'),
    path('delete_variant/<int:pk>/', views.delete_variant, name='delete_variant'),
]