from rest_framework import serializers
from apps.order.models import Product, OrderItem, OrderItemConfig

class ProductOrderItemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemConfig
        fields = ('id', 'order_item', 'key', 'value')

class ProductOrderItemSerializer(serializers.ModelSerializer):
    order_conf = ProductOrderItemConfigSerializer(many=True,read_only=True)
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'order_conf')
        
class ProductSerializer(serializers.ModelSerializer):
    # order_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # order_items = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='orderitem-detail')
    order_items = ProductOrderItemSerializer(many=True,read_only=True)
   
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_active', 'order_items')
        
   