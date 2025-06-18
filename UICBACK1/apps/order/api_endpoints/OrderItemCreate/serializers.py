from rest_framework import serializers
from apps.order.models import OrderItem, OrderItemConfig, Product, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'name',
        )
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order',
            'product',
            'quantity',
        )
        
    def to_internal_value(self, data):
        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order'] = OrderSerializer(instance.order).data
        return representation