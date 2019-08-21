from django.views.generic import (
    CreateView, ListView, DetailView, View,
    TemplateView, UpdateView, RedirectView)
from .forms import *
from api.models import Locations
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json


class ComplainDetailView(DetailView):
    model = Complain
    template_name = 'content.html'

    def form_valid(self, form):
        form.instance.complaine_id = self.request.complain.id
        return super(CommentCreateView, self).form_valid(form)

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
        comments = list(Comment.objects.filter(complain_id=self.object.id))
        context['comments'] = comments
        return context


class ComplainCreateView(CreateView):
    model = Complain
    form_class = ComplainForm
    template_name = 'complain_form.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(ComplainCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_location = Locations.objects.filter(author_id__exact=self.request.user.id)
        context['user_location'] = user_location.get()
        print(context['user_location'].id, context['user_location'].token, context['user_location'].author_id, context['user_location'].latitude, context['user_location'].longitude, )
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'content.html'

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


# complain list view
class ComplainListView(ListView):
    template_name = 'homepage.html'
    model = Complain

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        complain = list(Complain.objects.all())
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

        context['complains'] = complain
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


class IndexView(TemplateView):
    template_name = 'mainpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_location = Locations.objects.filter(author_id__exact=self.request.user.id)
        context['user_location'] = user_location.get()
        print(context['user_location'].id)
        return context


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile_form.html'
    success_url = '/index'

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(ProfileView, self).form_valid(form)


def post_like(request):
    pk = request.POST.get('pk', None)


# TODO : loginrequied 데코레이터에 certification 내용 추가 해서 사용할 수 있는지 확인해보기

class CertificationCreateView(CreateView):
    model = Locations
    template_name = 'certification.html'
    form_class = CertificationForm
    success_url = '/index'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(CertificationCreateView, self).form_valid(form)


class CertificationUpdateView(UpdateView):
    model = Locations
    template_name = 'certification.html'
    form_class = CertificationForm
    success_url = '/index'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super(CertificationUpdateView, self).form_valid(form)


class CertificationRedirectView(RedirectView):
    is_permanent = True

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
