from rest_framework.generics import ListAPIView
from .serializers import OrderItemSerializer
from apps.order.models import OrderItem

class OrderItemAPIListView(ListAPIView):
    queryset = OrderItem.objects.select_related('order', 'product').only('id', 'order__name','order__created_at', 'order__user', 'product__name', 'product__price', 'product__is_active', 'quantity')
    serializer_class = OrderItemSerializer
    
__all__ = [
    'OrderItemAPIListView',
]