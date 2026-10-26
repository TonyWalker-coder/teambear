from django.urls import path
from .views import home, account, logout, admin_panel, products, contact, specials, product_search

urlpatterns = [
    path("", home, name="home"),
    path("account/", account, name="account"),
    path("logout/", logout, name="logout"),
    path("admin-panel/", admin_panel, name="admin_panel"),
    path("products/", products, name="products"),
    path("contact/", contact, name="contact"),
    path("specials/", specials, name="specials"),
    path("product-search/", product_search, name="product_search"),
]