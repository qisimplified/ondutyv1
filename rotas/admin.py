from django.contrib import admin

from .models import Rota

# Register your models here.


class RotaAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'tier', 'is_published', 'rota')
	list_display_links = ('id', 'title')
	list_filter = ('title', )
	search_fields = ('id', 'title', 'description')
	list_per_page = 25
	list_editable = ('tier', 'is_published')



admin.site.register(Rota, RotaAdmin)