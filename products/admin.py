from django.contrib import admin

from .models import Car, Part

class PartAdmin(admin.ModelAdmin):
	list_display = ('part_name', 'get_car__str', 'part_storage_location', 'part_number', 'part_price', 'listed_on_ebay',)
	search_fields = ['part_name', 'car__car_manufacturer', 'car__car_model', 'car__car_registration', 'part_number','part_storage_location']

	def get_car__str(self, obj):
		return obj.car.__str__()
	get_car__str.short_description = 'Car Details'


admin.site.register(Car)
admin.site.register(Part, PartAdmin)