from django.urls import path
from .views import home, account, logout

urlpatterns = [
    path("", home, name="home"),
    path("account/", account, name="account"),
    path("logout/", logout, name="logout"),
]