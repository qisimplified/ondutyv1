from django.contrib import admin


from .models import *
from import_export.admin import ImportExportModelAdmin




class MasterrotaAdmin(ImportExportModelAdmin):
	list_display = (
		'id', 'date', 'day', 
		'person1shifts', 
		'person2shifts', 
		'person3shifts',
		'person4shifts',
		'person5shifts', 
		'person6shifts',
		'person7shifts',
		'person8shifts',
		'person9shifts',
		'person10shifts',
		'person11shifts',
		'person12shifts',
		'person13shifts',
		'person14shifts',
		'person15shifts',
		'person16shifts',
		'person17shifts',
		'person18shifts',
		'person19shifts',
		'person20shifts',
		'person21shifts',
		'person22shifts',
		'person23shifts',
		'person24shifts',
		'person25shifts',
		'person26shifts',
		'person27shifts',
		'person28shifts',
		'person29shifts',
		'person30shifts',)
	list_display_links = ('id',)
	list_filter = (
		'date',
		'person1shifts', 
		'person2shifts', 
		'person3shifts',
		'person4shifts',
		'person5shifts', 
		'person6shifts',
		'person7shifts',
		'person8shifts',
		'person9shifts',
		'person10shifts',
		'person11shifts',
		'person12shifts',
		'person13shifts',
		'person14shifts',
		'person15shifts',
		'person16shifts',
		'person17shifts',
		'person18shifts',
		'person19shifts',
		'person20shifts',
		'person21shifts',
		'person22shifts',
		'person23shifts',
		'person24shifts',
		'person25shifts',
		'person26shifts',
		'person27shifts',
		'person28shifts',
		'person29shifts',
		'person30shifts', )
	search_fields = ('id', 'date', 'day', 'person1shifts', 'person2shifts')
	list_per_page = 365
	list_editable = ()



admin.site.register(Masterrota, MasterrotaAdmin)