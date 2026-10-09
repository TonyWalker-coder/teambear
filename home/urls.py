from django.urls import path
from .views import home, account

urlpatterns = [
    path("", home, name="home"),
    path("account/", account, name="account"),
]