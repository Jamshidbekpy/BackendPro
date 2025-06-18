from rest_framework import serializers
from apps.order.models import OrderItem, Order, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_active')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'created_at', 'user')
        
class OrderItemSerializer(serializers.ModelSerializer):
    # order_inf1 = OrderSerializer(read_only=True, source='order')
    # order_inf2 = serializers.SerializerMethodField(method_name='get_order_info')
    product_data = ProductSerializer(read_only=True, source='product')
    order_data = OrderSerializer(read_only=True, source='order')
    class Meta:
        model = OrderItem
        fields = ('id', 'quantity', 'product_data', 'order_data','order')
        
    # def get_order_info(self, obj):
    #     return OrderSerializer(obj.order).data if obj.order else None