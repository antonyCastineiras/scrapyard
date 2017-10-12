from django.contrib import admin
from django.forms import inlineformset_factory

from .models import Car, Part, PartImage

class PartImageInline(admin.StackedInline):
	model = PartImage
	fields = ['image']

class PartAdmin(admin.ModelAdmin):
	list_display = ('part_name', 'get_car__str', 'part_storage_location', 'part_number', 'part_price', 'listed_on_ebay',)
	search_fields = ['part_name', 'car__car_manufacturer', 'car__car_model', 'car__car_registration', 'part_number','part_storage_location']
	inlines = [PartImageInline]

	def get_car__str(self, obj):
		return obj.car.__str__()
	get_car__str.short_description = 'Car Details'

class CarAdmin(admin.ModelAdmin):
	list_display = ('manufacturer_and_model', 'car_registration')
	search_fields = ['car_manufacturer', 'car_model', 'car_registration']


admin.site.register(Car, CarAdmin)
admin.site.register(Part, PartAdmin)