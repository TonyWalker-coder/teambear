from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
    


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    ground = models.CharField(max_length=100, blank=True)
    history = models.TextField(blank=True)

    def __str__(self):
        return self.team_name



class ProductType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class ProductDescription(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="descriptions"
    )

    item_name = models.CharField(
        max_length=100
    )

    class Meta:
        ordering = ["item_name"]

    def __str__(self):
        return self.item_name


class Product(models.Model):

    bear_name = models.CharField(max_length=100)

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to="products/"
    )

    alt_text = models.CharField(
        max_length=255
    )

    promo_text = models.CharField(
            max_length=50,
            blank=True
        )

    description = models.TextField()


    product_description = models.ForeignKey(
        ProductDescription,
        on_delete=models.PROTECT,
        related_name="products",
        null=False,
        blank=False,
    )

    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name="products",
        null=False,
        blank=False,
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="products",
        null=False,
        blank=False,
    )


    stock = models.PositiveIntegerField(default=0)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    special_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    discount_percent = models.PositiveIntegerField(
        default=0
    )

    def clean(self):
        if (
            self.product_description
            and self.product_type
            and self.product_description.product_type != self.product_type
        ):
            raise ValidationError(
                {
                    "product_description":
                    "Description must belong to the selected product type."
                }
            )
        
    class Meta:
        ordering = ["bear_name"]

    def save(self, *args, **kwargs):
            self.full_clean()
            super().save(*args, **kwargs)   

    def __str__(self):
        return self.bear_name

class Sale(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    sale_date = models.DateTimeField(
        auto_now_add=True
    )

    total = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f"Sale {self.id}"

class SaleItem(models.Model):
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="sale_items"
    )

    qty = models.PositiveIntegerField(default=1)

    price_paid = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product} x {self.qty}"


