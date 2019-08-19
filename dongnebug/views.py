from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView,
    TemplateView, UpdateView, FormView)
from django.contrib.auth.models import User
from django.urls import (reverse, reverse_lazy)
from django.utils import timezone
from datetime import timedelta
from dongnebug.models import Complain, Favorite, Comment, Sympathy
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

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(CommentCreateView, self).form_valid(form)


# complain list view
class ComplainListView(ListView):
    template_name = 'homepage.html'
    model = Complain

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = list(Complain.objects.all())
        context['complains'] = complain
        return context


class KnockedBukView(ListView):
    model = Sympathy
    template_name = 'knockedbuk.html'


    def get_queryset(self):
        sympathies = Sympathy.objects.filter(user_id__exact=self.request.user.id)

        knocked_complains = []
        for sympathy in sympathies:
            knocked_complains.append(sympathy.complain_id)
        print(self.request.user.id)
        print(sympathies)
        print(knocked_complains)
        return Complain.objects.filter(id__in=knocked_complains)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = self.get_queryset()
        # TODO : 현재 유저가 넣은 것만 볼수 있게 하자
        context['complains'] = complain
        return context


class NewComplainView(TemplateView):
    template_name = 'newcomplain.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = list(Complain.objects.filter())
        favorite = list(Favorite.objects.filter())

        comment = list(Comment.objects.filter())
        sympathy = list(Sympathy.objects.filter())
        context['complain'] = complain
        context['comments'] = comment

        context['favorite'] = favorite
        context['sympathy'] = sympathy
        return context


class SearchView(ListView):
    template_name = 'search.html'
    model = Complain

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = self.get_queryset()
        context['complains'] = complain
        return context

    def get_queryset(self):
        try:
            complain_name = self.request.GET.get('q')
        except:
            complain_name = ''
        if complain_name != ('' or None):
            complains = Complain.objects.filter(title__icontains=complain_name)
        else:
            complains = Complain.objects.all()
        print(complains)
        return complains


class UploadedComplainListView(ListView):
    template_name = 'uploadedbuk.html'
    model = Complain

    def get_queryset(self):
        return Complain.objects.filter(author_id__exact=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complains = self.get_queryset()
        context['complains'] = complains
        return context


class ShowComplainView(TemplateView):
    template_name = 'showcomplain.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = list(Complain.objects.filter())
        favorite = list(Favorite.objects.filter())

        comment = list(Comment.objects.filter())
        sympathy = list(Sympathy.objects.filter())
        context['complain'] = complain
        context['comments'] = comment

        context['favorite'] = favorite
        context['sympathy'] = sympathy
        return context


class IndexView(TemplateView):
    template_name = 'mainpage.html'


class ProfileView(TemplateView):
    template_name = 'profile_edit.html'
