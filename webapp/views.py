from django.shortcuts import render
from django.shortcuts import render_to_response
from webapp import models

def index(request):
	return render_to_response('list.html', {'title':'kormushka'})

