from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import User
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.views import View
from django.contrib import messages

User = get_user_model()
# Create your views here.

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        
        # send email and user 
        # https://localhost:8000/user/activation/uid64/<token>/
        
        current_site = get_current_site(self.request)
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activotion_link = f"{current_site.domain}/user/activation/{uid}/{token}/"
        message = render_to_string('email/activation.html', {
            'user': user,
            'activotion_link': activotion_link
        })
        
        send_mail(
            subject='Activate your account',
            message=message,
            from_email='jamshidbekdev04@gmail.com',
            recipient_list=[user.email],
            
        )
        
        
        return redirect('user:login')

class ActivationView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('user:login')
        else:
            messages.error(request, 'Invalid activation link')
            return render(request, 'user/login.html')