from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Locations(models.Model):

    author = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    token = models.CharField(max_length=100, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=17, null=True, default=0)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, null=True, default=0)

    def __str__(self):
        return "latitude = "+ str(self.latitude) + " " \
               + "longitude = " + str(self.longitude)


