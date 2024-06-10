
from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.Logout, name='logout'),
]
