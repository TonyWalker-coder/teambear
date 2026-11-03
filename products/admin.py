from django.contrib import admin
from .models import Team, ProductType, ProductDescription, Product, UserProfile


admin.site.register(Product)




@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "item_name",
        "product_type",
    ]

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
       'name',
    ]

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        'team_name',
    ]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "theme",
        "title",
        "phone",
    ]