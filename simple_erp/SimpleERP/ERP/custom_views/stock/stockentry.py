from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import masters,stock
from ERP.serializers.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from ERP.custom_views.common_functions import *
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from django.urls import reverse
from rest_framework import status
from django.template.loader import render_to_string  

row_per_page = settings.GLOBAL_SETTINGS['row_per_page']


@api_view(['GET', 'POST'])
def stockentry_create(request):
    if request.method == 'GET':
        return Response({'data':'', 'module':'Stock Entry'}, template_name='ERP/stock/stockentry/create_update.html')
    else:
        mutable = request.POST._mutable
        request.POST._mutable = True
        
        if not request.data.get("stockentry_id"):
            entry_date=db_store_date(request.POST['entry_date'])
            data={
                "entry_date":entry_date,
                "purpose":request.POST['purpose'],
                "warehouse_from":request.POST['warehouse_from'],
                "warehouse_to":request.POST['warehouse_from'],
                "description":request.POST['description'],
                }
            serializer = StockEntrySerializer(data=data)
            serializer.is_valid()
            if serializer.is_valid():
                user_id= session_user_id(request)
                date_modified=store_date_time()
                stock_entry=serializer.save(created_by=user_id,created_date=date_modified)
                stockentry_id=stock_entry.id
                
            else:
                stockentry_id=""
                error_details = []
                for key in serializer.errors.keys():
                    error_details.append({"field": key, "message": serializer.errors[key][0]})
                    data = {
                    "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                    }
        else:
            stockentry_id=request.data.get("stockentry_id")
        if stockentry_id:
            data_stock_entry_items={
                "stockentry":stockentry_id,
                "item":request.POST['item'],
                "qty":request.POST['qty'],
                "accepted_qty":request.POST['qty'],
                "rejected_qty":0,
                "accepted_status" :1,
                "warehouse_from":request.POST['warehouse_from'],
                "warehouse_to":request.POST['warehouse_from'],

                }
            serializer = Stockentry_itemsSerializer(data=data_stock_entry_items)
            serializer.is_valid()
            if serializer.is_valid():
                user_id= session_user_id(request)
                date_modified=store_date_time()
                stockentry_items=serializer.save(created_by=user_id,created_date=date_modified)
                stockentry_items_id=stockentry_items.id
                if request.POST['serial_nos']:
                    pass
                Serial_no_create(1,stockentry_items_id,serial_nos)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    
def Serial_no_create(ref_type,ref_id,serial_nos):
    pass
    
    
        
@api_view(['GET', 'POST'])
def stockentry_items(request):
    if request.is_ajax():
        data = []
        html = render_to_string('ERP/stock/stockentry/stockentry_items.html', {'data': data})
    return HttpResponse(html)
    
