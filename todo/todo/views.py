from django.shortcuts import render,redirect

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
    