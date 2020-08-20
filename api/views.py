# api/views.py

from rest_framework import generics, permissions
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from .serializers import PostSerializer, UserSerializer
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminOrReadOnly, )
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
