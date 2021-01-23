from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Preset(models.Model):
    locationName = models.CharField(max_length=100)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )
    objects = models.Manager()


class FavouritePlaces(models.Model):
    locationName = models.CharField(max_length=100)
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )
    objects = models.Manager()
