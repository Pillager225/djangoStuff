from django.http import HttpResponse
from django.template import loader

def Home(request):
	template = loader.get_template('templates/home.html')
	context = {
		# dict entries go here
	}
	return HttpResponse(template.render(context, request))
