from rest_framework.generics import CreateAPIView,DestroyAPIView,UpdateAPIView,ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from cart.apis.serializers import AddtoCartSerializer,OrderSerializer


class CartCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AddtoCartSerializer

    def perform_create(self, serializer):
        user= self.request.user
        serializer.save(user=user)
        return serializer

class CartDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AddtoCartSerializer
    model = serializer_class.Meta.model
    queryset= model.objects.all()


class CartListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = AddtoCartSerializer
    model = serializer_class.Meta.model
    queryset= model.objects.all()

class OrderAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user= self.request.user
        serializer.save(user=user)
        return serializer

class OrderDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = OrderSerializer
    model = serializer_class.Meta.model
    queryset= model.objects.all()

