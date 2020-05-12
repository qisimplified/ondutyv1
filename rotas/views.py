from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from masterrotas.choices import price_choices, bedroom_choices, state_choices
from .models import Rota

# Create your views here.
def index(request): 
	rotas = Rota.objects.order_by('-tier').filter(is_published=True)
	
	paginator = Paginator(rotas, 6)
	page = request.GET.get('page')
	paged_rotas = paginator.get_page(page)
	from masterrotas.choices import price_choices, bedroom_choices, state_choices

	context = {
		'rotas': paged_rotas
	}
	return render(request, 'rotas/rotalist.html', context)

def masterrota(request, rota_id):
	return render(request, 'rotas/masterrota.html')

def search(request):

	queryset_list = Rota.objects.order_by('-tier')

	# keywords
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)

	# rota
	if 'rota' in request.GET:
		rota = request.GET['rota']
		if keywords:
			queryset_list = queryset_list.filter(rota__iexact=rota)

	# date
	if 'date' in request.GET:
		date = request.GET['date']
		if keywords:
			queryset_list = queryset_list.filter(rota__iexact=date) # change rota__exact to date_iexact

	# person
	if 'person' in request.GET:
		person = request.GET['person']
		if keywords:
			queryset_list = queryset_list.filter(rota__iexact=person) # change rota__exact to person_iexact

	# shift
	if 'shift' in request.GET:
		shift = request.GET['shift']
		if keywords:
			queryset_list = queryset_list.filter(rota__iexact=shift) # change rota__exact to shift_iexact


	context = {
        'state_choices': state_choices, #change to my search choice dic in choices.py
        'bedroom_choices': bedroom_choices, #change to my search choice dic in choices.py
        'price_choices': price_choices, #change to my search choice dic in choices.py
        'rotas': queryset_list,
        'values': request.GET
    }
	return render(request, 'rotas/search.html')

