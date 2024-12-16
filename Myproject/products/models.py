from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
