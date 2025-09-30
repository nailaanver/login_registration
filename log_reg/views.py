from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get

# Create your views here.
