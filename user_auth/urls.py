
from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
]
