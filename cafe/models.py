from django.db import models


# Create your models here.
class Products(models.Model):
    pitem=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    prate=models.IntegerField(blank=True)
    pqty=models.CharField(max_length=100)
    banner=models.ImageField(upload_to='coffee_images/', blank=True, null=True)


    def __str__(self):
        return self.pitem
    
class Cart(models.Model):
    pitem=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    prate=models.IntegerField(blank=True)
    pqty=models.CharField(max_length=100)
    quandity=models.IntegerField(blank=True)    
    total=models.IntegerField(blank=True)
    name=models.CharField(max_length=100)


class Ordernow(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    streetaddress=models.CharField(max_length=100)    
    mobilenumber=models.IntegerField(blank=True)
    email=models.EmailField()
    totalvalue=models.IntegerField(blank=True)
    razorpay_order_id=models.CharField(max_length=100)
    razorpay_payment_id=models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)


class Post(models.Model):
        title=models.CharField(max_length=100)
        body=models.TextField()
        slug=models.SlugField()
        date=models.DateTimeField(auto_now_add=True)
        banner=models.ImageField(default='images.jpeg',blank=True)

        def __str__(self):
         return self.title
    
from django import forms
from django.contrib.auth.models import User




