from rest_framework import serializers
from .models import Post, Tag, Category


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "category", "author", "created_at")
        read_only_fields = ("id", "title", "category", "author", "created_at")


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "category",
            "author",
            "tags",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "category",
            "author",
            "tags",
            "created_at",
            "updated_at",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "category",
            "author",
            "tags",
            "created_at",
            "updated_at",
        )


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "content",
            "category",
            "author",
            "tags",
            "created_at",
            "updated_at",
        )


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
        read_only_fields = ("id", "name")


class CategoryDetailSerializer(serializers.ModelSerializer):

    posts = PostListSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "posts")
        read_only_fields = ("id", "name")


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id", "name")


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id", "name")


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)
        read_only_fields = "name"
