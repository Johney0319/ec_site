from django.db import models
from django.contrib.auth.models import AbstractUser

class Jackets(models.Model):
    jacket_id = models.CharField(max_length=10)
    jacket_name = models.CharField(max_length=20)
    jacket_price = models.IntegerField()
    jacket_size = models.CharField(max_length=2, blank=True, null=True)
    jacket_sex = models.CharField(max_length=5)
    jacket_bland = models.CharField(max_length=30)
    jacket_stock = models.CharField(max_length=3)
    jacket_image = models.ImageField(upload_to='images/')

class Shirts(models.Model):
    shirt_id = models.CharField(max_length=10)
    shirt_name = models.CharField(max_length=20)
    shirt_price = models.IntegerField()
    shirt_size = models.CharField(max_length=2, blank=True, null=True)
    shirt_sex = models.CharField(max_length=5)
    shirt_bland = models.CharField(max_length=30)
    shirt_stock = models.CharField(max_length=3)
    shirt_image = models.ImageField(upload_to='images/')

class Pants(models.Model):
    pant_id = models.CharField(max_length=10)
    pant_name = models.CharField(max_length=20)
    pant_price = models.IntegerField()
    pant_size = models.CharField(max_length=2, blank=True, null=True)
    pant_sex = models.CharField(max_length=5)
    pant_bland = models.CharField(max_length=30)
    pant_stock = models.CharField(max_length=3)
    pant_image = models.ImageField(upload_to='images/')

class Shoes(models.Model):
    shoe_id = models.CharField(max_length=10)
    shoe_name = models.CharField(max_length=20)
    shoe_price = models.IntegerField()
    shoe_size = models.CharField(max_length=2, blank=True, null=True)
    shoe_sex = models.CharField(max_length=5)
    shoe_bland = models.CharField(max_length=30)
    shoe_stock = models.CharField(max_length=3)
    shoe_image = models.ImageField(upload_to='images/')

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)
    coupon = models.IntegerField(default=0)

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

class CartItem(models.Model):
    jackets = models.ForeignKey(Jackets, on_delete=models.CASCADE, null=True)
    shirts = models.ForeignKey(Shirts, on_delete=models.CASCADE, null=True)
    pants = models.ForeignKey(Pants, on_delete=models.CASCADE, null=True)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    cart_sum = models.IntegerField(default=0, null=True)
    cart_coupon = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField()

class PurchaseHistory(models.Model):
    purchase_id = models.CharField(max_length=250, blank=True)
    purchase_user = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    purchase_sum = models.IntegerField(default=0, null=True)
    use_coupon = models.IntegerField(default=0, null=True)
    jackets_history = models.ForeignKey(Jackets, on_delete=models.CASCADE, null=True)
    shirts_history = models.ForeignKey(Shirts, on_delete=models.CASCADE, null=True)
    pants_history = models.ForeignKey(Pants, on_delete=models.CASCADE, null=True)
    shoes_history = models.ForeignKey(Shoes, on_delete=models.CASCADE, null=True)