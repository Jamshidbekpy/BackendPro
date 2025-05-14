from rest_framework import serializers
from .models import ContactUs


class ContactUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ("name", "email", "subject", "message")
