from django.urls import path
from .views import *
from . import views
app_name = 'mr'
urlpatterns = [
    path('stylelist/', stylelist.as_view(), name='stylelist'),
    path('buyerview/', buyerview.as_view(), name='buyerview'),
    path('buyer_stylelist/<int:id>/', buyer_stylelist.as_view(), name='buyer_stylelist'),
]