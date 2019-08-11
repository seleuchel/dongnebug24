from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class Complain(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        unique=True  # TODO : 어떤 효과인지 확인해보자
    )
    title = models.TextField()
    content = models.TextField()
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    num_of_sympathies = models.IntegerField(default=0)
    num_of_comments = models.IntegerField(default=0)
    is_complete = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)
    #TODO : Add Video attribute

    def __str__(self):
    #TODO : Check for security issue which is information leak
        return '__all__'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    complain = models.ForeignKey(
        Complain,
        on_delete=models.CASCADE
    )

    def __str__(self):
    #TODO : Check for security issue which is information leak
        return '__all__'


class ComplainImage(models.Model):
    complain = models.ForeignKey(
        Complain,
        on_delete=models.CASCADE
    )
    image = models.ImageField(blank=True)

    def __str__(self):
    #TODO : Check for security issue which is information leak
        return '__all__'


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    complain = models.ForeignKey(
        Complain,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
    #TODO : Check for security issue which is information leak
        return '__all__'


class Sympathy(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    complain = models.ForeignKey(
        Complain,
        on_delete=models.CASCADE
    )

    def __str__(self):
    #TODO : Check for security issue which is information leak
        return '__all__'
