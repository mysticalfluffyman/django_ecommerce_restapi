from django.shortcuts import render
from products.models import Category


def categories(request):
    category_list = Category.objects.all()
    return {"categories": category_list}

