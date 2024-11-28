from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Buyer(models.Model):
    BuyerName = models.CharField(max_length=225)
    Joined_Date = models.DateField()
    Address = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.BuyerName

class Style(models.Model):
    BuyerName = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    StyleCode = models.CharField(max_length=225,unique=True)
    ItemName = models.CharField(max_length=225,blank=True,null=True)
    barcode = models.CharField(max_length=225, blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.StyleCode

class Order(models.Model):
    BuyerName = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    StyleCode = models.ForeignKey(Style, on_delete=models.CASCADE)
    ItemName = models.CharField(max_length=225,blank=True,null=True)
    Qty = models.IntegerField(default=0)
    CMP = models.FloatField(default=0.00)
    ordered_date = models.DateField(blank=True,null=True)
    export_date = models.DateField(blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.StyleCode.StyleCode

class Accessories(models.Model):
    accessories_name = models.CharField(max_length=255, blank=True, null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.accessories_name





