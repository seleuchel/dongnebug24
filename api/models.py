from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    latitude = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    def __str__(self):
        return "latitude = "+ str(self.latitude) + " " \
               + "longitude = " + str(self.longitude)
