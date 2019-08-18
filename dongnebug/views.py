from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView,
    TemplateView,UpdateView, FormView)
from django.contrib.auth.models import User
from django.urls import (reverse, reverse_lazy)
from django.utils import timezone
from datetime import timedelta
from dongnebug.models import Complain, Favorite, ComplainImage, Comment, Sympathy
from . import models
from . import forms
from api.models import Locations
import random
from scipy.spatial import distance

def getComplains():
    near_complains = []
    user_latitude=Locations.objects.filter(id=73).values('latitude').first()['latitude']
    user_longitude=Locations.objects.filter(id=73).values('longitude').first()['longitude']
    complains = Complain.objects.all()
    for complain in complains:
        dist = distance.euclidean((float(complain.latitude), float(complain.longitude)), (float(user_latitude), float(user_longitude)),5)
        if dist < 0.05:
            near_complains.append(complain)
    return near_complains
    
#queryset = Complain.objects.filter(pk__in=getComplains())

class NewComplainView(TemplateView):
    template_name = 'new_complain.html'


    def get_absolute_url(self):
        return reverse('dongnebug:index')

class ContentView(TemplateView):
    form_class=forms.GetCommentForm
    template_name='content.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter(pk=kwargs['num']).values())
        favorite=list(Favorite.objects.filter(complain=kwargs['num']).values())
        image=list(ComplainImage.objects.filter(complain=kwargs['num']).values())
        comment=list(Comment.objects.filter(complain=kwargs['num']).values())
        sympathy=list(Sympathy.objects.filter(complain=kwargs['num']).values())
        context['complain']=complain[0]
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context

class HomepageView(TemplateView):
    form_class=forms.HomepageForm
    template_name='homepage.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter().values())
        favorite=list(Favorite.objects.filter().values())
        image=list(ComplainImage.objects.filter().values())
        comment=list(Comment.objects.filter().values())
        sympathy=list(Sympathy.objects.filter().values())
        context['complains']=complain
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context

class KnockedBukView(TemplateView):
    form_class=forms.KnockedBukForm
    template_name='knockedbuk.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter())
        favorite=list(Favorite.objects.filter())
        image=list(ComplainImage.objects.filter())
        comment=list(Comment.objects.filter())
        sympathy=list(Sympathy.objects.filter())
        context['complain']=complain
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context



class NewComplainView(TemplateView):
    form_class=forms.NewComplainForm
    template_name='newcomplain.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter())
        favorite=list(Favorite.objects.filter())
        image=list(ComplainImage.objects.filter())
        comment=list(Comment.objects.filter())
        sympathy=list(Sympathy.objects.filter())
        context['complain']=complain
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context

class SearchView(TemplateView):
    form_class=forms.SearchForm
    template_name='search.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter().values())
        favorite=list(Favorite.objects.filter().values())
        image=list(ComplainImage.objects.filter().values())
        comment=list(Comment.objects.filter().values())
        sympathy=list(Sympathy.objects.filter().values())
        context['complains']=complain
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context

class UploadBukView(TemplateView):
    form_class=forms.UploadBukForm
    template_name='uploadbuk.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter())
        favorite=list(Favorite.objects.filter())
        image=list(ComplainImage.objects.filter())
        comment=list(Comment.objects.filter())
        sympathy=list(Sympathy.objects.filter())
        context['complain']=complain
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context



class ShowComplainView(TemplateView):
    template_name='showcomplain.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        complain=list(Complain.objects.filter())
        favorite=list(Favorite.objects.filter())
        image=list(ComplainImage.objects.filter())
        comment=list(Comment.objects.filter())
        sympathy=list(Sympathy.objects.filter())
        context['complain']=complain
        context['comments']=comment
        context['image']=image
        context['favorite']=favorite
        context['sympathy']=sympathy
        return context