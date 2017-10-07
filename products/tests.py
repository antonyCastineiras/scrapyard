import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Car, Part

# Create your tests here.
class PartModelTests(TestCase):

	def test_part_exists_after_car_is_deleted(self):
		c = Car(created_at=timezone.now())
		c.save()
		p = Part(car=c, created_at=timezone.now())
		p.save()
		c.delete()
		self.assertIs(Part.objects.all().count(), 1)

class CarModelTests(TestCase):

	def test_mnufacturer_and_model_returns_full_name_capitalized(self):
		car = Car(car_manufacturer='subaru', car_model='impreza', created_at=timezone.now())
		self.assertEqual(car.manufacturer_and_model(), 'Subaru Impreza')

