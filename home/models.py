from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    ground = models.CharField(max_length=100, blank=True)
    history = models.TextField(blank=True)

    def __str__(self):
        return self.team_name


class ProductDetails(models.Model):
    title = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    size_unit = models.CharField(max_length=10)
    description = models.TextField()
    history = models.TextField(blank=True)

    def __str__(self):
        return self.title


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

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="products"
    )

    details = models.ForeignKey(
        ProductDetails,
        on_delete=models.PROTECT,
        related_name="products"
    )

    stock = models.PositiveIntegerField(default=0)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    special = models.BooleanField(default=False)

    special_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    discount_percent = models.PositiveIntegerField(
        default=0
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["bear_name"]

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


