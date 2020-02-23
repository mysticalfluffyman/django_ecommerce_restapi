from django.urls import path
from products.apis.api_views import(
    ProductsAddAPIView,
    CategoryCreateAPIView,
    ProductDeleteAPIView,
    ProductListAPIView,
    ProductsUpdateAPIView,
    ProductsRetriveAPIView,
    LikeAPIView,
    UnlikeAPIView,
    ReviewAPIView,
    ReviewDeleteAPIView,
    ReviewUpdateAPIView,
    CollectionAPIView,
    CollectionDeleteAPIView,
    CollectionUpdateAPIView,
    CollectionListAPIView,
)

urlpatterns=[
    path("addcategories/", CategoryCreateAPIView.as_view(),name='add_category'),
    path("",ProductsAddAPIView.as_view()),
    path("list/<pk>/delete/",ProductDeleteAPIView.as_view()),
    path("list/",ProductListAPIView.as_view()),
    path("list/<pk>/update/",ProductsUpdateAPIView.as_view()),
    path("list/<pk>/",ProductsRetriveAPIView.as_view()),
    path("list/like/",LikeAPIView.as_view()),
    path("list/like/<pk>/unlike",UnlikeAPIView.as_view()),
    path("list/review/",ReviewAPIView.as_view()),
    path("list/review/<pk>/update/",ReviewUpdateAPIView.as_view()),
    path("list/review/<pk>/delete/",ReviewDeleteAPIView.as_view()),
    path("collection/create/",CollectionAPIView.as_view()),
    path("collection/list/<pk>/delete/",CollectionDeleteAPIView.as_view()), 
    path("collection/list/<pk>/update/",CollectionUpdateAPIView.as_view()),
    path("collection/list/",CollectionListAPIView.as_view()),

    

]