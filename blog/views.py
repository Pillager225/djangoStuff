from django.http import HttpResponse
from django.template import loader
import psycopg2
import psycopg2.extras

def Home(request):
	template = loader.get_template('templates/home.html')
	blogEntries = []
	context = {}
	return HttpResponse(template.render(context, request))
'''	try:
		conn = psycopg2.connect("dbname='blogdb' user='slave' host='localhost' password='aSuperDuperPassword'")
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute("SELECT * FROM blogEntries;")
		rows = cursor.fetchall()
		for row in rows:
			pass	
	except Exception e as msg:
		print(msg)
	context = {
		'blogEntries' : blogEntries
	} '''

'''def BlogEntry(request):
	template = loader.get_template('templates/blogEntry' + blogEntryNum + '.html')
	context = {
		'title' : blogEntryTitle
	}
	return HttpResponse(template.render(context, request))
'''
