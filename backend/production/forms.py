# LineScheduleForm
from django import forms
from .models import *


class LineScheduleForm(forms.ModelForm):
    class Meta:
        model = LineSchedule
        fields = ['line','style_name', 'item', 'target_qty', 'total_qty', 'start_date', 'due_date', 'color', 'description']
        widgets = {
            'line': forms.Select(attrs={'class': 'form-control'}),
            'style_name': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'target_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_qty': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control w-50', 'type':'date'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control w-50', 'type':'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'color': forms.TextInput(attrs={'class': 'form-control form-control-color', 'type':'color'})
        }