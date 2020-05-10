from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin




class RotaAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'tier', 'is_published', 'rota')
	list_display_links = ('id', 'title')
	list_filter = ('title', )
	search_fields = ('id', 'title', 'description')
	list_per_page = 25
	list_editable = ('tier', 'is_published')



admin.site.register(Rota, RotaAdmin)