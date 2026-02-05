from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token #Vorgefertigte DRF View für Login mit Token-Response
from .views import UserRegistrationView

urlpatterns = [
    path('', obtain_auth_token, name='login'),
    path('login/', obtain_auth_token, name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]