from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login   # alias login

def login_view(request):   # only request, no user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # username = request.POST.get('username')
        # password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)   # use Django’s login
            return redirect('home')     # use name "home", not "home/"
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if not all([username, email, password, password_confirm]):
            return render(request, 'register.html', {'error': 'All fields are required'})
        if password != password_confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered.'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')   # redirect using URL name
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')
