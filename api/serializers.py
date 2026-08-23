from django.contrib.auth.models import Group, User
from rest_framework import serializers
from news_app.models import Tag, Category, Post, Contact, Newsletter, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {
            "email": {"required": True},
            "first_name": {"required": True},
        }
        fields = [
            "id",
            "username",
            "email",
            "groups",
            "first_name",
            "is_active",
            "is_superuser",
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "image",
            "author",
            "status",
            "view_count",
            "published_at",
            "category",
            "tags",
        ]
        extra_kwargs = {
            "author": {"read_only": True},
            "view_count": {"read_only": True},
            "published_at": {"read_only": True},
        }

    def validate(self, data):
        data["author"] = self.context["request"].user
        return data


class PostPublishSerializer(serializers.Serializer):
    post = serializers.IntegerField()


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
    
    

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "created_at", "updated_at","name", "email", "subject", "message"]

class NewsLetterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["id", "created_at", "updated_at", "email"]
