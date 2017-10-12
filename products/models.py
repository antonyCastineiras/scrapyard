import os
from django.db import models

# Create your models here.
class Car(models.Model):
	car_manufacturer = models.CharField(max_length=200)
	car_model = models.CharField(max_length=200)
	car_registration = models.CharField(max_length=200)
	car_notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField()

	def __str__(self):
		return (self.manufacturer_and_model() + ' - ' self.car_registration).title()

	def manufacturer_and_model(self):
		return self.car_manufacturer + ' ' + self.car_model

class Part(models.Model):
	car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
	part_name = models.CharField(max_length=200)
	part_number = models.CharField(max_length=200, blank=True, null=True)
	part_notes = models.TextField(blank=True, null=True)
	part_storage_location = models.CharField(max_length=200)
	part_price = models.DecimalField(max_digits=10,decimal_places=2)
	listed_on_ebay = models.BooleanField(default=False)
	created_at = models.DateTimeField()

	def __str__(self):
		if self.car:
			return self.car.manufacturer_and_model() + ' ' + self.part_name
		else:
			return self.part_name

class PartImage(models.Model):
	part = models.ForeignKey(Part, related_name='images',on_delete=models.CASCADE)
	image = models.ImageField()
