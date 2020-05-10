from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='rotalist'),
	path('<int:rota_id>', views.masterrota, name='masterrota'),
	path('search', views.search, name='search'),
]