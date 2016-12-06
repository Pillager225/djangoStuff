from django.http import HttpResponse
from django.template import loader
import psycopg2
import psycopg2.extras
import re

def Home(request):
	template = loader.get_template('templates/home.html')
	blogEntries = []
	try:
		conn = psycopg2.connect("dbname='blogdb' user='slave' host='localhost' password='aSuperDuperPassword'")
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute("SELECT * FROM blogEntries ORDER BY date ASC;")
		blogEntries = cursor.fetchall()
	except Exception as msg:
		print(msg)
	context = {
		'blogEntries' : blogEntries
	}
	return HttpResponse(template.render(context, request))

def BlogEntry(request, num='0'):
	loc = 'templates/entry' + num + '.html'
	row = {}
	try:
		conn = psycopg2.connect("dbname='blogdb' user='slave' host='localhost' password='aSuperDuperPassword'")
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute("SELECT * FROM blogEntries WHERE location = %s", (loc,))
		row = cursor.fetchone()
	except Exception as msg:
		print(msg)
	template = loader.get_template(loc)
	context = {
		'title' : row['title'],
		'image' : row['image']
	}
	return HttpResponse(template.render(context, request))
