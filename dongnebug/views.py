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
from .forms import *
from api.models import Locations
import random
from scipy.spatial import distance


class ComplainDetailView(DetailView):
    model = Complain
    template_name = 'content.html'


class ComplainCreateView(CreateView):
    model = Complain
    form_class = ComplainForm
    template_name = 'complain_form.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(ComplainCreateView, self).form_valid(form)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'content.html'
    success_url = 'index/'


class HomepageView(TemplateView):
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

class RegisterView(CreateView):
    template_name = 'login.html'
    success_url = reverse_lazy('login')


class IndexView(TemplateView):
    template_name = 'mainpage.html'
