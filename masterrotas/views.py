from django.shortcuts import render
from .models import *

# Create your views here.



def display_master_rota(request):
	items = Masterrota.objects.all()

	context = {
		'items': items,
	}

	return render (request, 'masterrotas/masterrota.html', context)