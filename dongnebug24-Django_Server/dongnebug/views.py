from django.views.generic import (
    CreateView, ListView, DetailView, View,
    TemplateView, UpdateView, RedirectView)
from .forms import *
from api.models import Locations
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
import json
from scipy.spatial import distance
from django.contrib.auth.mixins import LoginRequiredMixin


class ComplainDetailView(LoginRequiredMixin, DetailView):
    model = Complain
    template_name = 'content.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            sympathy = Sympathy.objects.filter(
                complain_id__exact=self.object.id,
                user_id__exact=self.request.user.id
            ).get()
            context['sympathy'] = sympathy
        except Exception:
            pass
        file = str(Complain.objects.filter(id=self.object.id).get().file)
        context['extension'] = file[file.rfind('.')+1:]
        comments = list(Comment.objects.filter(complain_id=self.object.id))
        context['comments'] = comments
        return context


def CommentCreateView(request, pk):
    form = CommentForm(request.POST or None)

    if form.is_valid() and pk:
        form.instance.author = request.user
        form.instance.request = Complain.objects.get(id=pk)
        form.save()
        return HttpResponseRedirect('/complain/' + str(request.object.pk))
    return HttpResponseRedirect('/complain/' + str(request.object.pk))



class ComplainCreateView(LoginRequiredMixin, CreateView):
    model = Complain
    form_class = ComplainForm
    template_name = 'complain_form.html'
    login_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(ComplainCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_location = Locations.objects.filter(author_id__exact=self.request.user.id)
        context['user_location'] = user_location.get()
        print(context['user_location'].id, context['user_location'].token, context['user_location'].author_id, context['user_location'].latitude, context['user_location'].longitude, )
        return context


# mixin 테스트
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'content.html'
    login_url = '/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.complaine_id = self.request.complain.id
        return super(CommentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = Complain.objects.filter(author_id__exact=self.request.user.id)
        comments = list(Comment.objects.filter(complain_id=complain.id))
        context['object'] = complain
        context['comments'] = comments
        print(complain, comments)
        return context


class ComplainListView(LoginRequiredMixin, ListView):
    template_name = 'homepage.html'
    model = Complain
    login_url = '/'

    def get_queryset(self):
        near_complains = []
        locations = Locations.objects.filter(author_id__exact=self.request.user.id)
        user_latitude = locations.values('latitude').first()['latitude']
        user_longitude = locations.values('longitude').first()['longitude']
        complains = Complain.objects.all().filter(is_complete=0)
        print(complains)
        for complain in complains:
            dist = distance.euclidean((float(complain.latitude), float(complain.longitude)),
                                      (float(user_latitude), float(user_longitude)), 5)
            if dist < 0.05:
                near_complains.append(complain.id)
        return Complain.objects.filter(id__in=near_complains)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = self.get_queryset()
        context['complains'] = complain
        return context


def complain_sympathy(request, pk):
    complain = get_object_or_404(Complain, pk=pk)
    complain_sympathy, created = Sympathy.objects.get_or_create(
        user_id=request.user.id,
        complain_id=complain.id
    )
    if not created:
        complain_sympathy.delete()

    context = {
        'sympathy_count': complain.sympathy_count,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


class KnockedBukView(LoginRequiredMixin, ListView):
    model = Sympathy
    template_name = 'knockedbuk.html'
    login_url = '/'

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

        context['complains'] = complain
        return context


class SearchView(LoginRequiredMixin, ListView):
    template_name = 'search.html'
    model = Complain
    login_url = '/'

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


class UploadedComplainListView(LoginRequiredMixin, ListView):
    template_name = 'uploadedbuk.html'
    model = Complain
    login_url = '/'

    def get_queryset(self):
        return Complain.objects.filter(author_id__exact=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complains = self.get_queryset()
        context['complains'] = complains
        return context


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'mainpage.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_location = Locations.objects.filter(author_id__exact=self.request.user.id)
        context['user_location'] = user_location.get()
        print(context['user_location'].id)
        return context


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile_form.html'
    success_url = '/index'
    login_url = '/'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(ProfileView, self).form_valid(form)


def post_like(request):
    pk = request.POST.get('pk', None)


# TODO : loginrequied 데코레이터에 certification 내용 추가 해서 사용할 수 있는지 확인해보기

class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Locations
    template_name = 'certification.html'
    form_class = CertificationForm
    success_url = '/index'
    login_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(CertificationCreateView, self).form_valid(form)


class CertificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Locations
    template_name = 'certification.html'
    form_class = CertificationForm
    success_url = '/index'
    login_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(CertificationUpdateView, self).form_valid(form)


class CertificationRedirectView(LoginRequiredMixin, RedirectView):
    is_permanent = True
    login_url = '/'

    def get_redirect_url(self, *args, **kwargs):

        user_location = Locations.objects.filter(author_id__exact=self.request.user.id)
        if user_location:
            return '/certification/update/' + str(user_location.get().id)
        else:
            return '/certification/create/'

# TODO : 'content.html' 초기 위치를 디비에서 가져와서 사용하기
# TODO : 근처 민원 기능 추가
# TODO : 이미 디비에 토큰이 저장 되어 있다면 CreateView가 아니라, UpdateView를 통해 할 수 있도록 바꾼다.
# TODO : 공감 기능 추가
# TODO : 댓글 기능 추가
