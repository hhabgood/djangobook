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

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	if offset > 1:
		hourVal = "hours"
	else: 
		hourVal = "hour"
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s %s it will be %s</body></html>" % (offset, hourVal, dt)
	return HttpResponse(html)