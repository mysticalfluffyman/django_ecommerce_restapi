from rest_framework import serializers
from accounts.models import User, Profile
from django.db import transaction

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField()


class ProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "dob", "address", "contact_num"


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerailizer()
    

    class Meta:
        model = User
        fields = "first_name", "last_name", "email", "username", "password", "role", "profile"
    
    @transaction.atomic
    def create(self, validate_data):
        profile = validate_data.pop("profile")
        raw_password = validate_data.pop("password")
        user = User(**validate_data)
        user.set_password(raw_password)
        user.save()
        Profile.objects.create(**profile, user=user)
        return user

class SocialSerializer(serializers.Serializer):
    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)

"""
Serializer which accepts an OAuth2 access token and provider.

"""
    
"""{
    "first_name": "anuj", 
    "last_name": "subedi", 
    "profile": {
        "dob": 24324/54543/45, 
        "address": "ktm"
    }
}"""