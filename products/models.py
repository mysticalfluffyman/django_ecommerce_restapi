from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.title

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    catagory = models.ManyToManyField(Category, related_name='product_category')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    #image = models.ImageField(upload_to='news',null = True)
    slug = models.SlugField(max_length= 255, null=True)

    def get_absolute_url(self):
        return reverse("product",kwargs={"pk":self.pk, "slug":self.slug})
    
    def countno(self):
        return self.count


class Reviews(models.Model):
    product = models.ForeignKey(Products,on_delete = models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL,null= True)
    review = models.TextField()
    count = models.IntegerField(default=0)

class Productlike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.SET_NULL,null = True)
    product = models.ManyToManyField(Products, related_name= 'liked_product')

class Collection(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.SET_NULL,null = True)
    product = models.ManyToManyField(Products, related_name= 'collection')
    slug = models.SlugField(max_length= 255, null=True)