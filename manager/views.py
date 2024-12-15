from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import *


def index(request: WSGIRequest):
    brands = Brand.objects.all()
    cars = Cars.objects.all()

    context = {
        "brands": brands,
        "cars": cars
    }

    return render(request, "index.html", context)


def detail_brand(request: WSGIRequest):
    car = Cars.objects.all()
    brands = Brand.objects.all()
    context = {
        'cars': car,
        'brands': brands
    }

    return render(request, "index.html", context)


def detail_cars(request: WSGIRequest):
    car = Cars.objects.all()
    context = {
        'cars': car
    }

    return render(request, "car.html", context)
