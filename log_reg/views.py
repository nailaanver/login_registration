from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def login(request):
    return render(request,'login.html')
def register_user(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password_confirm = request.POST['password_confirm']
        
    #     if not all([username,email,password,password_confirm]):
    #         return render(request,'register.html',{'error': 'All fields are required'})
    #     if password != password_confirm:
    #         return render(request,'register.html',{'error':'Passwords do not match.'})
    #     if User.objects.filter(username = username).exists():
    #         return render (request,'register.html',{'error':'Username already taken.'})
    #     if User.objects.filter(email=email).exists():
    #         return render(request,'register.html',{'error':'Email already registered.'})
        return render(request,'register.html')
                          
# Create your views here.
