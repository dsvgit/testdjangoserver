from django.shortcuts import render
from django.shortcuts import render_to_response
from webapp import models

def index(request):

	p1 = models.Purchase.objects.all()
	return render_to_response('list.html', {'title':'kormushka','purchase': p1})

