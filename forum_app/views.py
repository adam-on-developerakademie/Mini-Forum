from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.

class PostListCreateView(generics.ListCreateAPIView):       #GET (Liste) + POST (Erstellen)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):       #Wird bei POST requests automatisch aufgerufen
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):       #GET (Detail) + PUT/PATCH (Update) + DELETE (Löschen)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):       #GET (Liste) + POST (Erstellen)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):       #Wird bei POST requests automatisch aufgerufen
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):       #GET (Detail) + PUT/PATCH (Update) + DELETE (Löschen) 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    
