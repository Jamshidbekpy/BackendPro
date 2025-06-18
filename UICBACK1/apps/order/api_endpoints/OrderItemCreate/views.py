from rest_framework.generics import CreateAPIView
from .serializers import OrderItemCreateSerializer

class OrderItemCreateAPIView(CreateAPIView):
    serializer_class = OrderItemCreateSerializer
    
    