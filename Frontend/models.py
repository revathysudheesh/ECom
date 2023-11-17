from django.db import models

# Create your models here.
class UserDB(models.Model):
    UserName=models.CharField(max_length=20, null=True, blank=True)
    UserEmail=models.EmailField(max_length=200, null=True, blank=True)
    UserContact=models.IntegerField(null=True, blank=True)
    UserPassword=models.CharField(max_length=20, null=True, blank=True)
    Image=models.ImageField(upload_to='UserImages', null=True, blank=True)

class CartDB(models.Model):
    UserName =models.CharField(max_length=20, null=True, blank=True)
    ProName=models.CharField(max_length=20, null=True, blank=True)
    Description=models.CharField(max_length=200, null=True, blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    TotalPrice=models.IntegerField(null=True, blank=True)

class BillingAddressDB(models.Model):
    UserName = models.CharField(max_length=20, null=True, blank=True)
    BillingFirstName=models.CharField(max_length=20, null=True, blank=True)
    BillingLastName=models.CharField(max_length=20, null=True, blank=True)
    BillingCompanyName=models.CharField(max_length=20, null=True, blank=True)
    BillingMail=models.EmailField(max_length=100, null=True, blank=True)
    BillingAddress1=models.CharField(max_length=100, null=True, blank=True)
    BillingAddress2=models.CharField(max_length=100, null=True, blank=True)
    BillingCity=models.CharField(max_length=100, null=True, blank=True)
    BillingState=models.CharField(max_length=100, null=True, blank=True)
    BillingContact=models.IntegerField(null=True, blank=True)
    BillingPincode=models.IntegerField(null=True, blank=True)
    BillingComments=models.CharField(max_length=200, null=True, blank=True)
