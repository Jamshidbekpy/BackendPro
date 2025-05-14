from rest_framework.response import Response
from .models import ContactUs
from .serializers import ContactUsCreateSerializer
from apps.users.generics import CreateAPIView


class ContactUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsCreateSerializer
