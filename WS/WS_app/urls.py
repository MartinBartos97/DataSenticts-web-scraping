from django.urls import path
from WS_app import views

urlpatterns = [
    path("", views.car_list, name="car_list"),
]
