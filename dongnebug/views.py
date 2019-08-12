from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView,
    TemplateView,UpdateView, FormView)
from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView
from django.urls import (reverse, reverse_lazy)
from django.utils import timezone
from datetime import timedelta
from . import models
from . import forms
import random

# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = forms.AccountForm
#     model = User
#
#     def form_valid(self, form):
#         form.save()
#         return super(LoginView, self).form_valid(form)
#
#     def get_absolute_url(self):
#         return reverse('login')

class IndexView(TemplateView):
    template_name = 'login.html'


class RegisterView(CreateView):
    form_class = forms.RegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')


