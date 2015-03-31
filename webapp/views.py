from django.shortcuts import render
#from webapp.models import Purchase
from django.contrib import auth
from django.core.context_processors import csrf

def index(request):

#	purchase = Purchase.objects.all() #получение всех покупок
	return render(request,'list.html', {
		'title':'kormushka',
		'user':auth.get_user(request),
	})