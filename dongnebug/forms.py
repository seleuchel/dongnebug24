from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Complain, Favorite, Comment, Sympathy

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=( 'content',)


class SearchForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complain
        fields = ('title', 'content', 'file', 'latitude', 'longitude')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'id': 'text'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'id': 'text'
                }
            ),
        }



