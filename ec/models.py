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
