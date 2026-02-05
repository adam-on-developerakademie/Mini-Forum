from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer

# Create your views here.

class UserRegistrationView(generics.CreateAPIView): #Generic APIView für User-Registrierung
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]  # Anyone can register
    
    def create(self, request, *args, **kwargs): #Überschreibt die Create-Methode, um Token zurückzugeben
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create token for the new user
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'token': token.key,
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)
        