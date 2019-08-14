from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView,
    TemplateView,UpdateView, FormView)
from django.contrib.auth.models import User
from django.urls import (reverse, reverse_lazy)
from django.utils import timezone
from datetime import timedelta
from . import models
from . import forms
import random

class RegisterView(CreateView):
    form_class = forms.RegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')


class IndexView(TemplateView):
    template_name = 'index.html'


class CreateComplainView(CreateView):
    form_class = forms.ComplainForm
    template_name = 'new_complain.html'


    def get_absolute_url(self):
        return reverse('dongnebug:index')





