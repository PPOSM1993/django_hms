from django import forms
from django.contrib.auth.forms import UserCreationForm

from user_auth.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Full Name', "class": "a custom class"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Email'
    }))
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone']