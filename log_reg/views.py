from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout  # alias login
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='login') # Redirects to 'login' URL if not authenticated
def home(request):
    username = request.user.username  # Get the username of the logged-in user
    context = {'username': username}
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')
