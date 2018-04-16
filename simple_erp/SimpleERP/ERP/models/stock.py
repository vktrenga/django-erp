from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.core.exceptions import NON_FIELD_ERRORS
from .masters import *
#from ERP.masters import  *

class StockEntry(models.Model):
    """docstring for StateMaster"""
    entry_date = models.DateTimeField()
    purpose=models.IntegerField(default=0)
    warehouse_from=models.ForeignKey(
        WareHouse, on_delete=models.CASCADE, blank=True, null=True,related_name="StockEntry_Warehouse_From_WareHouse")
    warehouse_to=models.ForeignKey(
        WareHouse, on_delete=models.CASCADE, blank=True, null=True,related_name="StockEntry_Warehouse_To_WareHouse")
    description=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,default=1,related_name="StockEntry_Created_By_User")
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,default=1,related_name="StockEntry_Modified_By_User")
    deleted = models.BooleanField(default=False)
     
class Stockentry_items(models.Model):
    stockentry=models.ForeignKey(
    StockEntry, on_delete=models.CASCADE, blank=False, null=False)
    item=models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=False, null=False)
    qty=models.FloatField(default=0)
    accepted_qty=models.FloatField(default=0)
    rejected_qty=models.FloatField(default=0)
    accepted_status=models.IntegerField(default=0)
    accepted_by = models.ForeignKey(
        User, on_delete=models.CASCADE,default=1)
    warehouse_from=models.ForeignKey(
        WareHouse, on_delete=models.CASCADE, blank=True, null=True,related_name="Stockentry_items_Warehouse_From_WareHouse")
    warehouse_to=models.ForeignKey(
        WareHouse, on_delete=models.CASCADE, blank=True, null=True,related_name="Stockentry_items_Warehouse_To_WareHouse")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Stockentry_items_Created_By_User")
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Stockentry_items_Modified_By_User")
    deleted = models.BooleanField(default=False)
    
class Serial_no(models.Model):
    item=models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=False, null=False)
    serial_no=models.CharField(max_length=250,unique=True)
    status=models.IntegerField(default=0) # 1 store / 2 out / 3 blocked for 
    warehouse=models.ForeignKey(WareHouse,on_delete=models.CASCADE,default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,default=1)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Serial_no_Created_By_User")
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Serial_no_Modified_By_User")
    deleted = models.BooleanField(default=False)
    
    
class Serial_no_tracking(models.Model):
    item=models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=False, null=False)
    serial_no_id=models.ForeignKey(Serial_no,on_delete=models.CASCADE,default=1)
    ref_type=models.IntegerField(default=0)
    ref_id=models.IntegerField(default=0)
    warehouse=models.ForeignKey(WareHouse,on_delete=models.CASCADE,default=1)
    ref_name=models.CharField(max_length=100,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Serial_no_tracking_Created_By_User")
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Serial_no_tracking_Modified_By_User")
    company=models.ForeignKey(Company,on_delete=models.CASCADE,default=1)
    deleted = models.BooleanField(default=False)    


class Stock(models.Model):
    item=models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=False, null=False)
    current_stock=models.FloatField(default=0)
    blocked_stock=models.FloatField(default=0)
    warehouse=models.ForeignKey(WareHouse,on_delete=models.CASCADE,default=1)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,default=1)
    deleted = models.BooleanField(default=False)    

class Stock_Tracking(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE, blank=False, null=False)
    qty=models.FloatField(default=0)
    ref_type=models.IntegerField(default=0)
    ref_id=models.IntegerField(default=0)
    warehouse=models.ForeignKey(WareHouse,on_delete=models.CASCADE,default=1)
    ref_name=models.CharField(max_length=100,blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name='Stock_Tracking_Created_By_User')
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE,  default=1,related_name="Stock_Tracking_Modified_By_User")
    company=models.ForeignKey(Company,on_delete=models.CASCADE,default=1)
    deleted = models.BooleanField(default=False)    
    
    
    
    
    
    
    