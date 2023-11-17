from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    CatName=models.CharField(max_length=20, null=True, blank=True)
    Description=models.CharField(max_length=200, null=True, blank=True)
    Image=models.ImageField(upload_to='CatImages', null=True, blank=True)

class ProductDB(models.Model):
    CatName=models.CharField(max_length=20, null=True, blank=True)
    ProName=models.CharField(max_length=20, null=True, blank=True)
    Description=models.CharField(max_length=200, null=True,blank=True)
    Proprice=models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to="ProductImages", null=True, blank=True)