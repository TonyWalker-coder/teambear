from django.shortcuts import render

def home(request):
    return render(request, "home/home.html")

def account(request):
    return render(request, "account/account.html")

def signup(request):
    return render(request, "account/signup.html")
