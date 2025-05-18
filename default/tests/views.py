from rest_framework.generics import GenericAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# for email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str    
from django.core.mail import EmailMessage
from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_active=False)

        # Send activation email
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        subject = 'Activate Your Account'
        # message = f'Please activate your account at http://{current_site.domain}/tests/activate/{uid}/{token}/'
        message = f"""
        <html>
            <body>
                <h2>Welcome to Our Site!</h2>
                <p>Hi <strong>{user.username}</strong>,</p>
                <p>Thank you for registering. Please activate your account by clicking the link below:</p>
                <p><a href="http://{current_site.domain}/tests/activate/{uid}/{token}/" style="padding:10px 20px; background-color:#4CAF50; color:white; text-decoration:none; border-radius:5px;">
                Activate Account</a></p>
                <p>If you did not register, please ignore this email.</p>
                <br>
                <p>Best regards,<br>Your Website Team</p>
            </body>
        </html>
        """
        email = EmailMessage(subject, message, 'jamshidbekshodibekov2004@gmail.com', [user.email])
        email.content_subtype = "html"  # Emailni HTML sifatida jo'natish uchun
        email.body = message
        email.send()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
class ActivationView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Activation successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Activation link is invalid'}, status=status.HTTP_400_BAD_REQUEST)


        
        
        
        
        
        
    

