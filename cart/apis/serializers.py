from rest_framework import serializers
from cart.models import AddtoCart ,Order
from accounts.apis.serializers import UserSerializer
from products.apis.serializers import ProductsSerializer
from products.models import Products


class AddtoCartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only= True)
    product= ProductsSerializer(read_only= True, many= True)
    products_id = serializers.PrimaryKeyRelatedField(
        write_only= True, many =True, queryset = Products.objects.all(),source= 'product'
    )
    class Meta:
        model= AddtoCart
        fields= ("id","user","product","products_id")

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only= True)
    cart= AddtoCartSerializer(read_only= True, many= True)
    cart_id = serializers.PrimaryKeyRelatedField(
        write_only= True, many =True, queryset = AddtoCart.objects.all(),source= 'cart'
    )
    class Meta:
        model= Order
        fields= ("id","user","cart","cart_id")