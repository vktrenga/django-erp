from datetime import datetime
from django import template
register = template.Library()
from ERP.models.masters import *
from django.db import connection

@register.simple_tag
def current_year():
	#return "Something"
    return datetime.now().strftime("%Y")

@register.simple_tag
def application_name():
	return "Simple ERP | Admin"

@register.simple_tag
def show_single_field(tableName,show_field_name,pk):
	data = []
	with connection.cursor() as cursor:
		query = "SELECT  `%s` FROM %s where id=%s" %(show_field_name,tableName,pk)
		#return query
		cursor.execute(query)
		row = cursor.fetchone()
		return row[0]
		


@register.simple_tag
def drop_down_list(tableName,show_field_name,store_field_name):
	data = []
	with connection.cursor() as cursor:
		query = "SELECT %s, %s FROM %s where deleted='0'" %(store_field_name,show_field_name,tableName)
		#return query
		cursor.execute(query)
		rows = cursor.fetchall()
		for obj in rows:
			data.append({"id":(obj[0]),"text":(obj[1])})
		return data