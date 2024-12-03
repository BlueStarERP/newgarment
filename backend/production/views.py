from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,UpdateView
from django.http import JsonResponse

from .models import *
from mr.models import *

from .forms import *
# Create your views here.

class ScheduleView(View):
    def get(self, request):
        line = LineName.objects.all()
        return render(request, 'pro/ScheduleView.html', {'lid':2, 'line':line})

class ScheduleByLine(View):
    def get(self, request, id):
        line = LineName.objects.get(id=id)
        return render(request, 'pro/ScheduleByLine.html', {'lid':id, 'line':line, 'title':line.line_name})


class ScheduleData(View):
    def get(self, request,id):
        line = LineName.objects.get(id=id)
        schedules = LineSchedule.objects.filter(line=line)
        schedule_list =[]
        for data in schedules:
            schedule_list.append({
                'title':f'{data.style_name.StyleCode}'+ ' [target :' + f'{data.target_qty}' +']'+' [Desc :' + f'{data.description}' +']',
                'start': data.start_date.isoformat() if data.start_date else None,
                'end': data.due_date.isoformat() if data.due_date else None,
                'description': 'description for All Day Event',
                'url': 'http://127.0.0.1:8000/pro/ScheduleDetail/' + f'{data.id}',
                # 'display': 'background',
                'color': data.color,
            })
        return JsonResponse(schedule_list, safe=False)

class ScheduleDetail(View):
    def get(self, request, id):
        context ={}
        obj = get_object_or_404(LineSchedule, id = id)
        form = LineScheduleForm(request.GET or None, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('production:ScheduleView')
 
    # add form dictionary to context
        context["form"] = form
 
        return render(request, "pro/ScheduleDetail.html", context)
    

class ProductionLineList(View):
    def get(self, request):
        line = LineName.objects.all()
        context = {'line':line, 'title':'ProductionLineList'}
        return render(request, "pro/ProductionLineList.html", context)

class LineinputAcc(View):
    def get(self, request):
        style = Style.objects.all()
        line = LineName.objects.get(adminuser=request.user)
        usr = request.user
        inputacc1 = LineInputAcc.objects.filter(approved=1, line=line)
        inputacc2 = LineInputAcc.objects.filter(approved=2, line=line)
        context = {'title':'Accessories Issues Request', 'style':style, 'inputacc1':inputacc1, 'inputacc2':inputacc2}
        return render(request, "pro/LineinputAcc.html", context)
    
    def post(self, request):
        line = LineName.objects.get(adminuser=request.user)
        stylename = request.POST.get('stylename')
        item = request.POST.get('item')
        qty = request.POST.get('qty')
        style_obj = Style.objects.get(id=stylename)
        acc = LineInputAcc.objects.create(line= line, request_by= request.user,style_name= style_obj, item=item, request_qty=qty)
        return redirect(request.META['HTTP_REFERER'])