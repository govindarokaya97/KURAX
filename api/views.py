from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from api.serializers import (
    GroupSerializer,
    UserSerializer,
    TagSerializer,
    CategorySerializer,
    PostSerializer,
    PostPublishSerializer,
)
from news_app.models import Tag, Category, Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404



class PostPublishViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostPublishSerializer

    def post(self, request, *args, **kwargs):
        print("========== PUBLISH ==========")
        print("REQUEST DATA:", request.data)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_id = serializer.validated_data["post"]

        post = get_object_or_404(
            Post,
            id=post_id,
            published_at__isnull=True
        )

        post.published_at = timezone.now()
        post.save(update_fields=["published_at"])

        return Response(
            PostSerializer(post).data,
            status=status.HTTP_200_OK
        )


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]    #For everyone



class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):

        # get(list), get(id--retrive), post(create), put(update), patch(partialupdate), delete(destory)
        if self.action in ["list"]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()



class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ["list", "retrieve"]:
            queryset = queryset.filter(published_at__isnull=False, status="active")
        return queryset

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()


