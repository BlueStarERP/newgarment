from django.db import models
from mr.models import *
from django.contrib.auth.models import User
# Create your models here.

class LineName(models.Model):
    line_name = models.CharField(max_length=255)
    target = models.PositiveIntegerField(default=0)
    redcolor = models.PositiveIntegerField(default=0)
    successcolor = models.PositiveIntegerField(default=0)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.line_name

class LineSchedule(models.Model):
    line = models.ForeignKey(LineName, on_delete=models.CASCADE)
    style_name = models.ForeignKey(Style, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=True, null=True)
    target_qty = models.IntegerField(default=0)
    total_qty = models.IntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    complete_date = models.DateField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScheduleNote(models.Model):
    schedule = models.ForeignKey(LineSchedule, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LineHandover(models.Model):
    line = models.ForeignKey(LineName, on_delete=models.CASCADE)
    style_name = models.ForeignKey(Style, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=True, null=True)
    input_qty =models.IntegerField(default=0)
    handover_qty =models.IntegerField(default=0)
    input_date = models.DateField()
    handover_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class LineInput(models.Model):
    line = models.ForeignKey(LineName, on_delete=models.CASCADE)
    request_by = models.ForeignKey(User, on_delete=models.CASCADE)
    style_name = models.ForeignKey(Style, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=True, null=True)
    request_qty =models.IntegerField(default=0)
    input_qty =models.IntegerField(default=0)
    request_date = models.DateTimeField(auto_now_add=True)
    approved = models.IntegerField(default=1)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
