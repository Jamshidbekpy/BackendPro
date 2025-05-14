from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name", "bio"]


class ChangePasswordSerializer(serializers.ModelSerializer):
    coniform_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = ["password", "coniform_password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def validate_password(self, value):
        data = self.get_initial()
        assert data["password"] == data["coniform_password"]
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        # Username va passwordni attrs dan olish
        username = attrs.get("username")
        password = attrs.get("password")

        # Foydalanuvchini qidirish
        user = User.objects.filter(
            username=username
        ).first()  # first() faqat birinchi foydalanuvchini qaytaradi

        # Agar foydalanuvchi mavjud va parol to'g'ri bo'lsa
        if user and check_password(password, user.password):
            attrs["user"] = user  # Foydalanuvchini attrs ga qo'shamiz
            return attrs

        # Xatolikni qaytarish, agar foydalanuvchi yoki parol noto'g'ri bo'lsa
        raise serializers.ValidationError("Invalid credentials")
