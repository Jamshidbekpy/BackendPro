from rest_framework import serializers
from apps.order.models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'is_active')
        
    def validate(self, attrs):
        if attrs['price'] < 0:
            raise serializers.ValidationError({"price":"Price must be greater than zero"})
        
        if attrs['name'] and len(attrs['name']) > 5:
            raise serializers.ValidationError({"name":"Name must be a string"})
        
        return attrs
    
    def validate_price(self, value):
        if value < 3:
            raise serializers.ValidationError("Price must be greater than zero")
        return value