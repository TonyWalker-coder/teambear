from django.urls import path
from .views import home, account, signup, logout

urlpatterns = [
    path("", home, name="home"),
    path("account/", account, name="account"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout"),
]