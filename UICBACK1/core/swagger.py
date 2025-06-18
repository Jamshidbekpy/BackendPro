from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path, re_path
from django.contrib import admin

schema_view = get_schema_view(
   openapi.Info(
      title="Sizning API nomi",
      default_version='v1',
      description="Swagger hujjatlari",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jamshidbekdev04@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)