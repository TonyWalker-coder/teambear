from django.urls import path
from .views import home, account, logout, admin_panel, products

urlpatterns = [
    path("", home, name="home"),
    path("account/", account, name="account"),
    path("logout/", logout, name="logout"),
    path("admin-panel/", admin_panel, name="admin_panel"),
    path("products/", products, name="products"),
]