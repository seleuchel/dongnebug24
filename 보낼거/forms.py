from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Complain, Favorite, ComplainImage, Comment, Sympathy

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('user', 'complain', 'content', 'pub_date')



class SearchForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")



#<!-- Edit by sumin start -->
class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('title', 'content', 'file','latitude', 'longitude')
        labels = {
            'title' : '',
            'content' : '',
            'file' : '',
            'latitude' : '',
            'longitude' : ''
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'size' : '20',
                    'class' : 'form-control',
                    'placeholder' : "위치를 찾아보세요."
                }

            ),
            'content': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "내용을 입력하세요",
                    'aria-label' : "With textarea"
                }
            ),
            'latitude' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "위도"
                }
            ),
            'longitude' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : "경도"
                }
            )

        }
        
#<!-- Edit by sumin end -->

