from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryDeleteView,
    TagListView,
    TagDetailView,
    TagCreateView,
    TagDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path("category-list/", CategoryListView.as_view(), name="category-list"),
    path(
        "category-detail/<int:pk>", CategoryDetailView.as_view(), name="category-detail"
    ),
    path("category-create/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "category-delete/<int:pk>", CategoryDeleteView.as_view(), name="category-delete"
    ),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("tag-detail/<int:pk>", TagDetailView.as_view(), name="tag-detail"),
    path("tag-create/", TagCreateView.as_view(), name="tag-create"),
    path("tag-delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),
    path("post-list/", PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post-create/", PostCreateView.as_view(), name="post-create"),
    path("post-update/<int:pk>", PostUpdateView.as_view(), name="post-update"),
    path("post-delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
]
