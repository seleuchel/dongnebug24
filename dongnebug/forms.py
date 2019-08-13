from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Complain


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True',
        }
    ))
    username = forms.RegexField(label="Username", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and "
                                          "@/./+/-/_ only.",
                                error_messages={
                                    'invalid': "This value may contain only letters, numbers and "
                                               "@/./+/-/_ characters."},
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Username',
                                    'required': 'true',
                                }))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ("author", "title", "content")
        # TODO : Add latitude, longitude, images, videos




# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')

