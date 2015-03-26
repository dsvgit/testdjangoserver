from django.shortcuts import render
from django.shortcuts import render_to_response
from webapp import models

def index(request):

	p1 = models.Purchase.objects.all()
	p2 = models.Organization.objects.all()
	org = None
	r = list(p2[:1])
	if r:
	  org = r[0]
	return render_to_response('list.html', {'title':'kormushka','purchase': p1,'organization':org})