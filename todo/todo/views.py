from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import todoo
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username,email,password)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')

        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
    