from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Complain(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.TextField()
    content = models.TextField()
    latitude = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=17, null=True)
    file = models.FileField(upload_to='./')
    # like_user_set = models.ManyToManyField(
    #     User,
    #     blank=True,
    #     related_name='like_user_set',
    #     through='like'
    # )
    num_of_comments = models.IntegerField(default=0)
    #TODO : num_of_sympathy 구현 :: AJAX로 디비 연동까지
    is_complete = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    # @property
    # def sympathy_count(self):
    #     return self.like_user_set.count()

    def __str__(self):
    #TODO : Check for security issue which is information leak
        return self.title

    def get_absolute_url(self):
        return reverse('dongnebug:complain_detail', args=[self.id])



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
        return (self.author.username if self.author else "무명") + "의 댓글"

    def get_absolute_url(self):
        return reverse('dongnebug:complain_detail', args=[self.complain_id])


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
