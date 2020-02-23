from django.urls import path,include
from accounts.apis.api_views import UserRegistrationAPIView,SocialLoginAPIView

# urls
urlpatterns = [
    path("register/", UserRegistrationAPIView.as_view(), name="user_register"),
    path("socialauth/login/",SocialLoginAPIView.as_view(),name = "social_auth"),
   
]