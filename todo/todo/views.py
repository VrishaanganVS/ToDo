from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import todoo

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username,email,password)
        
        my_user = User.objects.create(username,email,password)
        my_user.save()
        return redirect('login.html')
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
    