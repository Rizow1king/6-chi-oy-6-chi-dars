from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='home'),
    path('brands/<int:brand_id>/', detail_brand, name='brand_detail'),
    path('cars/<int:cars_id>', detail_cars, name='car_detail')
]
