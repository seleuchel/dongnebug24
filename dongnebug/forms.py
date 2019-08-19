from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Complain, Favorite, ComplainImage, Comment, Sympathy

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('user', 'complain', 'content', 'pub_date')


class HomepageForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")
class NewComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")
class SearchForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")
class UploadBukForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")
class KnockedBukForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")


class ComplainForm(forms.ModelForm):

    class Meta:
        model = Complain
        fields = ('title', 'content', 'latitude', 'longitude')
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



