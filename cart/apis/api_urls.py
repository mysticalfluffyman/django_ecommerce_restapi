from django.urls import path
from cart.apis.api_views import CartCreateAPIView,CartDeleteAPIView,CartListAPIView,OrderAPIView,OrderDeleteAPIView

urlpatterns=[
    path("",CartCreateAPIView.as_view()),
    path("list/",CartListAPIView.as_view()),
    path("list/<pk>/delete/",CartDeleteAPIView.as_view()),
    path("order/",OrderAPIView.as_view()),
    path("order/<pk>/delete",OrderDeleteAPIView.as_view()),


]