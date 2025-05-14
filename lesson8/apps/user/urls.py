from django.urls import path
from .views import RegisterView,ActivationView
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'user'


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activation/<uid64>/<token>/', ActivationView.as_view(), name='activation'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    
]