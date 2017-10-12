import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Car, Part

# Create your tests here.
class PartModelTests(TestCase):

	def test_part_exists_after_car_is_deleted(self):
		p = create_part()
		p.car.delete()
		self.assertIs(Part.objects.all().count(), 1)

class CarModelTests(TestCase):

	def test_manufacturer_and_model_returns_full_name(self):
		car = Car(car_manufacturer='subaru', car_model='impreza', created_at=timezone.now())
		self.assertEqual(car.manufacturer_and_model(), 'subaru impreza')


def create_car(car_manufacturer="test_car",car_model="test_car", car_registration="test",created_at=timezone.now()):
	car = Car(car_manufacturer=car_manufacturer, car_model=car_model, car_registration=car_registration, created_at=created_at)
	car.save()
	return car

def create_part(car=create_car(), part_name="test_part", part_number="123456", part_notes=None, part_storage_location='a1', part_price=.01, listed_on_ebay=False, created_at=timezone.now()):
	part = Part(car=car,part_name=part_name,part_number=part_number,part_storage_location=part_storage_location,part_price=part_price,listed_on_ebay=listed_on_ebay,created_at=created_at)
	part.save()
	return part

