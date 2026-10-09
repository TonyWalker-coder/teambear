from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("about/", include("about.urls")),
    path("accounts/", include("allauth.urls")),
]
