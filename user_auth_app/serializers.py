from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserRegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True) #Extra Feld zur Passwort-Bestätigung
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, data):   #Custom Validation für Passwort-Match und Eindeutigkeit
        # Check if passwords match
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError("Passwords don't match.")
        
        # Check if username is unique
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        
        # Check if email is unique
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        
        return data
    
    def create(self, validated_data): #Erstellt User mit gehashtem Passwort
        # Remove repeated_password as it's not needed for user creation
        validated_data.pop('repeated_password')
        
        # Create user with hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user