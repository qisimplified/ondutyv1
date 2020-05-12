from django.shortcuts import render
from .models import *

# Create your views here.



def display_master_rota(request):
	items = Masterrota.objects.all()

	context = {
		'items': items,
	}

	return render (request, 'masterrotas/masterrota.html', context)






# Create your views here.
def index(request): 
	rotas = Rota.objects.order_by('-tier').filter(is_published=True)
	
	paginator = Paginator(rotas, 6)
	page = request.GET.get('page')
	paged_rotas = paginator.get_page(page)

	context = {
		'rotas': paged_rotas
	}
	return render(request, 'rotas/rotalist.html', context)

# def masterrota(request, rota_id):
#	return render(request, 'rotas/masterrota.html')

def search(request):
	return render(request, 'rotas/search.html')