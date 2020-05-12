from django.shortcuts import render
from django.http import HttpResponse
from masterrotas.choices import price_choices, bedroom_choices, state_choices

from rotas.models import Rota

# Create your views here.


def index(request):
    rotas = Rota.objects.order_by('-tier').filter(is_published=True)[:3]

    context = {
        'rotas': rotas,
        'state_choices': state_choices, #change to my search choice dic in choices.py
        'bedroom_choices': bedroom_choices, #change to my search choice dic in choices.py
        'price_choices': price_choices, #change to my search choice dic in choices.py
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
