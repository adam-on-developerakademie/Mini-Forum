from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):      #Automatische Serializer-Generierung basierend auf Model
    author = serializers.StringRelatedField(read_only=True)        # Zeigt `str()` Representation statt ID
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']       #Felder die nicht vom Client gesetzt werden können


class CommentSerializer(serializers.ModelSerializer):      #Automatische Serializer-Generierung basierend auf Model
    author = serializers.StringRelatedField(read_only=True)        # Zeigt `str()` Representation statt ID
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'text', 'author', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']       #Felder die nicht vom Client gesetzt werden können
        
