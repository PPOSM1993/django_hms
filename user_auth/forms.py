from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_auth.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Full Name', "class": "a custom class form-control form-control-md"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username', "class": "a custom class form-control form-control-md"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Email', "class": "a custom class form-control form-control-md"
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Phone', "class": "a custom class form-control form-control-md"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', "class": "a custom class form-control form-control-md"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password', "class": "a custom class form-control form-control-md"
    }))

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone', 'password1', 'password2']