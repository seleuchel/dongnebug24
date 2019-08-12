from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2', )
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')

