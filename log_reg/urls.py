from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.login_view, name='login'),
    # path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home, name='home'),



]