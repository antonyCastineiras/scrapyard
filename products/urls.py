from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
	url(r'^parts/$', views.parts_index, name='parts_index'),
	url(r'^cars/$', views.cars_index, name='cars_index'),
	url(r'cars/(?P<car_id>[0-9]+)/$', views.car_detail, name='car_detail'),
	url(r'parts/(?P<part_id>[0-9]+)/$', views.part_detail, name='part_detail'),
]