from rest_framework.generics import CreateAPIView, DestroyAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.apis.serializers import CategoryListSerializer,ProductsSerializer,LikesSerializer,ReviewSerializer,CollectionSerializer
from django.utils.text import slugify

class ProductsAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes= [JWTAuthentication]
    serializer_class = ProductsSerializer

    def perform_create(self, serializer):
        print (serializer.validated_data)
        name = serializer.validated_data['name']
        slug = slugify(name)
        seller = self.request.user
        serializer.save(seller = seller,slug = slug)
        return serializer

class CategoryCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer

    def perform_create (self, serializer):
        title = serializer.validated_data['title']
        serializer.save(title=title)
        return serializer

class ProductDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

class ProductListAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class = ProductsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

class ProductsRetriveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    

   
        

class ProductsUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProductsSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

class LikeAPIView(CreateAPIView):
    permission_classes= [IsAuthenticated]
    authentication_classes= [JWTAuthentication]
    serializer_class = LikesSerializer
    def perform_create(self, serializer):
        user= self.request.user
        serializer.save(user=user)
        return serializer

class UnlikeAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = LikesSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

class ReviewAPIView(CreateAPIView):
    permission_classes= [IsAuthenticated]
    authentication_classes= [JWTAuthentication]
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        user= self.request.user
        serializer.save(reviewer=user)
        return serializer

class ReviewUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ReviewSerializer
    model= serializer_class.Meta.model
    queryset = model.objects.all()
    
class ReviewDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ReviewSerializer
    model= serializer_class.Meta.model
    queryset = model.objects.all()

class CollectionAPIView(CreateAPIView):
    permission_classes= [IsAuthenticated]
    authentication_classes= [JWTAuthentication]
    serializer_class = CollectionSerializer
    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        slug = slugify(name)
        user= self.request.user
        serializer.save(user=user, slug= slug)
        return serializer

class CollectionUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CollectionSerializer
    model= serializer_class.Meta.model
    queryset = model.objects.all()
    
class CollectionDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = CollectionSerializer
    model= serializer_class.Meta.model
    queryset = model.objects.all()

class CollectionListAPIView(ListAPIView):
    permission_classes=[AllowAny]
    serializer_class = CollectionSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()



