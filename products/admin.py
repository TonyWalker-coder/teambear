from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Team, ProductType

admin.site.register(Team)
admin.site.register(ProductType)