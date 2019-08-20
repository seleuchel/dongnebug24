from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Complain, Favorite, Comment, Sympathy
from api.models import Locations


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class SearchForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('title', 'content', 'file', 'latitude', 'longitude')
        labels = {
            'title': '',
            'content': '',
            'latitude': '',
            'longitude': ''
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'size': '20',
                    'class': 'form-control',
                    'placeholder': "위치를 찾아보세요."
                }

            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "내용을 입력하세요",
                    'aria-label': "With textarea"
                }
            ),
            'latitude': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "위도"
                }
            ),
            'longitude': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "경도"
                }
            ),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': "컴공의 누군가",
                    'style': "font-family:'Nanum Gothic', sans-serif"
                }
            )
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ('token', )


