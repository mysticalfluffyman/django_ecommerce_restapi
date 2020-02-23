from django.db import models
from products.models import Products
from django.conf import settings

from django.contrib.auth.models import User

class AddtoCart(models.Model):
    product= models.ManyToManyField(Products,related_name= "cart_products")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)

class Order(models.Model):
    cart = models.ForeignKey(AddtoCart,on_delete= models.CASCADE,null= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
