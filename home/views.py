from django.shortcuts import render 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from products.models import Team, ProductType, ProductDescription, Product

from django.http import JsonResponse
from django.template.loader import render_to_string


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
            product_count=Count("products", distinct=True)
        )
        .filter(product_count__gt=0)
        .order_by("team_name")
    )



    product_types = (
        ProductType.objects
        .prefetch_related("descriptions")
        .annotate(
            product_count=Count("descriptions", distinct=True)
        )
        
        .filter(product_count__gt=0)
    )

    for team in teams:
        team.product_types = (
            ProductType.objects
            .filter(products__team=team)
            .annotate(
                product_count=Count(
                    "products",
                    distinct=True
                )
            )
        .order_by("name")
        )

    descriptions = (
        ProductDescription.objects
        .annotate(
            product_count=Count("products")
        )
        .filter(product_count__gt=0)
    )

    description_count = (
        ProductDescription.objects
        .filter(products__isnull=False)
        .distinct()
        .count()
    )

    return render(
        request,
        "products/products_grid.html",
        {
            
            "teams": teams,
            "product_types": product_types,
            "descriptions": descriptions,
            "description_count": description_count,
        }

    )



# Product_grid bear cards

def product_search(request):

    

    team = request.GET.get("team")
    product_type = request.GET.get("type")
    desc = request.GET.get("desc")

    print("Search:", team, product_type, desc)

    products = Product.objects.all()



    if team and team != "all":
        products = products.filter(
            team__team_name=team
        )

    if product_type and product_type != "all":
        products = products.filter(
            product_type__name=product_type
        )


    if desc and desc != "all":
        products = products.filter(
            product_description__item_name=desc
        )

    products = products.order_by(
        "product_type__name",
        "product_description__item_name",
        "team__team_name",
    )

    html = render_to_string(
        "products/bear_cards.html",
        {"products": products}
    )

    return JsonResponse({
        "html": html,
        "count": products.count(),
    })