from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def login(request): # Renamed to avoid conflict with imported login function
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or dashboard after successful login
            return redirect('home') # Assuming 'home' is a defined URL name
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if not all([username,email,password,password_confirm]):
            return render(request,'register.html',{'error': 'All fields are required'})
        if password != password_confirm:
            return render(request,'register.html',{'error':'Passwords do not match.'})
        if User.objects.filter(username = username).exists():
            return render (request,'register.html',{'error':'Username already taken.'})
        if User.objects.filter(email=email).exists():
            return render(request,'register.html',{'error':'Email already registered.'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login') # Redirect to login page after successful registration
    return render(request, 'register.html')
                          
# Create your views here.
