from django.shortcuts import render
from WS_app.models import Car
from WS_app.Scrape import scrape


def car_list(request):
    scrape()
    cars = Car.objects.all()
    return render(request, "WS_app/car_list.html", {"cars": cars})
