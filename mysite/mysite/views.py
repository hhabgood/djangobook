from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("Hello World")

def homepage(request):
	return HttpResponse("<b>This is the homepage.</b>")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)