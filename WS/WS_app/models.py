from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    img_url = models.URLField()
    location = models.CharField(max_length=200)