from django.shortcuts import render
from django.http import HttpResponse

from .models import Part, Car
# Create your views here.

def parts_index(request):
	parts = Part.objects.all()
	return render(request, 'products/part_index.html', {'parts': parts})

def cars_index(request):
	cars = Car.objects.all()
	return render(request, 'products/car_index.html', {'cars': cars})

def car_detail(request, car_id):
	car = Car.objects.get(pk=car_id)
	return render(request, 'products/car_detail.html', {'car': car})

def part_detail(request, part_id):
	part = Part.objects.get(pk=part_id)
	return render(request, 'products/part_detail.html', {'part': part})