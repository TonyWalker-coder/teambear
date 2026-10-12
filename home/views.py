from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request):
    return render(request, "home/home.html")

def account(request):
    return render(request, "account/account.html")

def logout(request):
    return render(request, "account/logout.html")

@login_required
@user_passes_test(lambda u: u.is_staff)

def admin_panel(request):
    return render(request, "account/admin_panel.html")

def products(request):
    return render(request, "products_grid.html")