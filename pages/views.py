from django.shortcuts import render
from django.http import HttpResponse

from rotas.models import Rota

# Create your views here.
def index(request):
	rotas = Rota.objects.order_by('-tier').filter(is_published=True)[:3]

	context = {
		'rotas': rotas
	}
	return render(request, 'pages/index.html', context)

def about(request):
	return render(request, 'pages/about.html')
