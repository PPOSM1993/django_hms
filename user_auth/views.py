from django.shortcuts import render, redirect
from user_auth.models import User, Profile
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in.")
        return redirect("hotel:index")
    
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()

        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        password = form.cleaned_data.get("password1")

        user = authenticate(email=email, password=password)
        login(request, user)

        messages.success(request, f"Hey {full_name}, your account has been created successfully")

        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        return redirect("hotel:index")
    
    context = {
        "form": form
    }
    return render(request, "user_auth/sign-up.html", context)

def LoginView(request):
    pass