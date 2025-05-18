from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email','confirm_password')
    
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user