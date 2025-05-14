from apps.users.generics import (
    CreateAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DeleteAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Tag, Category
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryCreateSerializer,
    TagListSerializer,
    TagDetailSerializer,
    TagCreateSerializer,
)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryCreateSerializer


class CategoryDeleteView(DeleteAPIView):
    queryset = Category.objects.all()


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer


class PostDeleteView(DeleteAPIView):
    queryset = Post.objects.all()


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer


class TagCreateView(CreateAPIView):
    serializer_class = TagCreateSerializer


class TagDeleteView(DeleteAPIView):
    queryset = Tag.objects.all()










