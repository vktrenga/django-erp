from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import *
from ERP.serializers.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime

def session_user_id(request):
	user=request.session['_auth_user_id']
	user_id= User.objects.get(id=1)
	return user_id

def store_date_time():
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S')