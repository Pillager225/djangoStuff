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
		cursor.execute("SELECT * FROM blogEntries ORDER BY date DESC;")
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
		'image' : row['image'],
		'date' : row['date']
	}
	return HttpResponse(template.render(context, request))

def About(request):
	template = loader.get_template('templates/about.html')
	context = {
		'title' : "About Ryan",
		'image' : "/blog/img/me.jpg",
		'date' : ""
	}
	return HttpResponse(template.render(context, request))

def Contact(request):
	template = loader.get_template('templates/contact.html')
	context = {
		'title' : "Contact Ryan",
		'image' : "",
		'date' : ""
	}
	return HttpResponse(template.render(context, request))
	
def Question(request):
	template = loader.get_template('templates/question.html')
	context = {
		'title' : "Questions for Ryan",
		'image' : "",
		'date' : ""
	}
	return HttpResponse(template.render(context, request))
