from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)

    def __str__(self):
        return "latitude = "+ str(self.latitude) + " " \
               + "longitude = " + str(self.longitude)
