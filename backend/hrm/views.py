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


from django.forms import modelformset_factory
from django.urls import reverse


def test(request):
    context = {'title':'Home Page'}
    return render(request, 'hrm/department.html', context)

class departmentview(View):
    def get(self, request):
        dept = department.objects.all()
        form = departmentform()
        context = {'dept':dept, 'form':form ,'title':'DepartmentList'}
        return render(request, 'hrm/department.html', context)
    
    def post(self, request):
        dept_name = request.POST.get('department_name')
        d = department(department_name=dept_name)
        d.save()
        return redirect(request.META['HTTP_REFERER'])

class department_delete(View):
    def get(self, request,id):
        lid = request.GET.get('lid')
        dept = get_object_or_404(department,id=id)
        dept.delete()
        return JsonResponse({'status':'success'})

class positionview(View):
    def get(self, request):
        positions = position.objects.all()
        form = positionform()
        context = {'positions':positions,'title':'Positon List', 'form':form}
        return render(request, 'hrm/positionview.html', context)
    
    def post(self, request):
        posi = request.POST.get('position')
        d = position(position=posi)
        d.save()
        return redirect(request.META['HTTP_REFERER'])
    
class employeeview(View):
    def get(self, request):
        emp = employee_profile.objects.all()
        form = positionform()
        context = {'emp':emp,'title':'Employee List', 'form':form}
        return render(request, 'hrm/employeeview.html', context)


class createemployee(View):
    def get(self, request):
        form = positionform()
        context = {'title':'Employee Create', 'form':form}
        return render(request, 'hrm/createemployee.html', context)
    


class EmployeeCreate(CreateView):
    template_name = 'hrm/createemployee.html'
    form_class = employee_profile_form
    success_url = reverse_lazy('hrm:employeeview')


class EmployeeDetailView(DetailView):
    # specify the model to use
    model = employee_profile
    template_name = 'hrm/employee_detail.html'
 
    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["msg"] = "MISC"        
        return context






class EmpProfileInline():
    form_class = employee_profile_form
    model = employee_profile
    template_name = "hrm/createemployee.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('hrm:employeeview')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.employee_name = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.employee_name = self.object
            image.save()


class EmpCreate(EmpProfileInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(EmpCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': EduFormSet(prefix='variants'),
                'images': WorkexpFormSet(prefix='images'),
            }
        else:
            return {
                'variants': EduFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': WorkexpFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }


class EmpUpdate(EmpProfileInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(EmpUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': EduFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'images': WorkexpFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
        }
    

def delete_image(request, pk):
    try:
        image = Image.objects.get(id=pk)
    except Image.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('products:update_product', pk=image.product.id)

    image.delete()
    messages.success(
            request, 'Image deleted successfully'
            )
    return redirect('products:update_product', pk=image.product.id)


def delete_variant(request, pk):
    try:
        variant = Variant.objects.get(id=pk)
    except Variant.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('products:update_product', pk=variant.product.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('products:update_product', pk=variant.product.id)