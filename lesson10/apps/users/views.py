from .serializers import RegisterSerializer, ChangePasswordSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from .generics import CreateAPIView, UpdateAPIView, CheckAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


# class LoginView(CheckAPIView):
#     queryset = User.objects.all()
#     serializer_class = LoginSerializer


# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         instance = User.objects.all()
#         serializer = LoginSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
