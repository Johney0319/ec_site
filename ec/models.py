from django.db import models

# Create your models here.

class Jackets(models.Model):
    jacket_id = models.CharField(max_length=10)
    jacket_name = models.CharField(max_length=20)
    jacket_price = models.CharField(max_length=10)
    jacket_size = models.CharField(max_length=2)
    jacket_sex = models.CharField(max_length=5)
    jacket_bland = models.CharField(max_length=30)
    jacket_image = models.ImageField(upload_to='images/')

class Shirts(models.Model):
    shirt_id = models.CharField(max_length=10)
    shirt_name = models.CharField(max_length=20)
    shirt_price = models.CharField(max_length=10)
    shirt_size = models.CharField(max_length=2)
    shirt_sex = models.CharField(max_length=5)
    shirt_bland = models.CharField(max_length=30)
    shirt_image = models.ImageField(upload_to='images/')

class Pants(models.Model):
    pant_id = models.CharField(max_length=10)
    pant_name = models.CharField(max_length=20)
    pant_price = models.CharField(max_length=10)
    pant_size = models.CharField(max_length=2)
    pant_sex = models.CharField(max_length=5)
    pant_bland = models.CharField(max_length=30)
    pant_image = models.ImageField(upload_to='images/')

class Shoes(models.Model):
    shoe_id = models.CharField(max_length=10)
    shoe_name = models.CharField(max_length=20)
    shoe_price = models.CharField(max_length=10)
    shoe_size = models.CharField(max_length=2)
    shoe_sex = models.CharField(max_length=5)
    shoe_bland = models.CharField(max_length=30)
    shoe_image = models.ImageField(upload_to='images/')

