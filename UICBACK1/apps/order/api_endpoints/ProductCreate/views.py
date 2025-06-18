from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import ProductCreateSerializer
from apps.order.models import Product
from rest_framework import status

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer





__all__ = [
    'ProductCreateAPIView',
]