from django.shortcuts import render 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from products.models import Team, ProductType

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
    return render(request, "products/products_grid.html")

def contact(request):
    return render(request, "contact.html")

def specials(request):
    return render(request, "products/specials.html")

# Product_grid topPanel cards
def products(request):

    teams = (
        Team.objects
        .annotate(
            product_count=Count("products")
        )
        .filter(product_count__gt=0)
        .order_by("team_name")
    )

    product_types = (
        ProductType.objects
            .annotate(
                product_count=Count("products")
        )
        .filter(product_count__gt=0)
        .order_by("name")
    )

    return render(
        request,
        "products/products_grid.html",
        {
            "teams": teams,
            "product_types": product_types,
        }
    )



