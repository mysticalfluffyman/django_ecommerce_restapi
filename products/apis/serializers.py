from rest_framework import serializers
from products.models import Category, Products, Productlike, Reviews,Collection
from accounts.models import User
from accounts.apis.serializers import UserSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "title"


class ProductsSerializer(serializers.ModelSerializer):
    catagory = CategoryListSerializer(read_only=True, many=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        write_only=True, many=True, queryset=Category.objects.all(), source="catagory"
    )
    seller = UserSerializer(read_only=True)

    class Meta:
        model = Products
        fields = (
            "id",
            "name",
            "price",
            "count",
            "quantity",
            "catagory",
            "category_ids",
            "seller",
        )


class LikesSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(read_only=True, many=False)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Products.objects.all(), source="product"
    )
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = ("id", "user", "product", "product_id")


class ReviewSerializer(serializers.ModelSerializer):

    product = ProductsSerializer(read_only=True, many=False)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Products.objects.all(), source="product"
    )
    reviewer = UserSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = ("id", "reviewer", "review", "product", "product_id", "count")

class CollectionSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(read_only=True, many=True)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True,many = True ,queryset=Products.objects.all(), source="product"
    )
    user = UserSerializer(read_only=True)

    class Meta:
        model = Collection
        fields = ("id", "user", "product", "product_id", "name")


