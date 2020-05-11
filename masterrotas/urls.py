from django.urls import path

from . import views

urlpatterns = [
	path('', views.display_master_rota, name='masterrota'),
]