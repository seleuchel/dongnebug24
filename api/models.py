from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Locations(models.Model):
    '''
    authorid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    '''
    # author대신 토큰?
    
    latitude = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, null=True)

    def __str__(self):
        return "latitude = "+ str(self.latitude) + " " \
               + "longitude = " + str(self.longitude)

class PushToken(models.Model):
    #user = models.ForeignKey(
     #   User,
     #   on_delete=models.CASCADE,
    #)
    token = models.CharField(max_length=100, null = True)

    def __str__ (self):
        return str(self.token)
