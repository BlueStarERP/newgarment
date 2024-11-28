from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from .models import *
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,UpdateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
from django.contrib import messages

# Create your views here.
class stylelist(View):
    def get(self, request):
        style = Style.objects.all()
        context = {'title':'Style List', 'style':style}
        return render(request, 'mr/stylelist.html', context)

class buyerview(View):
    def get(self, request):
        buyer = Buyer.objects.all()
        style = Style.objects.all()
        context = {'title':'Style List', 'buyer':buyer, 'style':style}
        return render(request, 'mr/buyer.html', context)
# stylecode=&items=&cmp=
class buyer_stylelist(View):
    def get(self, request, id):
        buyer = Buyer.objects.all()
        style = Style.objects.filter(BuyerName=id)
        buyer_obj = Buyer.objects.get(id=id)
        message = None
        context = {'title':'Style List', 'buyer':buyer, 'style':style, 'buyer_obj':buyer_obj, 'message':message}
        return render(request, 'mr/buyer_stylelist.html', context)
    
    def post(self, request, id):
        buyer_obj = Buyer.objects.get(id=id)
        stylecode = request.POST.get('stylecode')
        items = request.POST.get('items')
        sty = Style.objects.create(BuyerName=buyer_obj, StyleCode=stylecode, ItemName=items)       
        return redirect(request.META['HTTP_REFERER'])