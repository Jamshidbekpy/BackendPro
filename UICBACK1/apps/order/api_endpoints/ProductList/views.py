from apps.order.models import Product, OrderItem, OrderItemConfig
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer
from django.db.models import Prefetch
class ProductAPIListView(ListAPIView):
    queryset = Product.objects.filter(order_items__isnull=False).prefetch_related(
        Prefetch(
            'order_items',
            queryset=OrderItem.objects.only(
                'id', 'order','quantity', 'product'
                )
            ),
            Prefetch(
                'order_items__order_conf',
                queryset=OrderItemConfig.objects.only('key', 'value')
            )
        )
    serializer_class = ProductSerializer

__all__ = [
    'ProductAPIListView',
    ]