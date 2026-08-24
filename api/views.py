from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from api.serializers import (
    GroupSerializer,
    UserSerializer,
    TagSerializer,
    CategorySerializer,
    PostSerializer,
    PostPublishSerializer,
    CommentSerializer,
    ContactSerializer,
    NewsLetterSerializer
)
from news_app.models import Tag, Category, Post, Contact, Comment, Newsletter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
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


class DraftListViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset= queryset.filter(published_at__isnull = True)

        return queryset


class PostListByCategoryViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False,
            status="active",
            category_id=self.kwargs["category_id"]
        )


class PostListByTagViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False,
            status="active",
            tags__id=self.kwargs["tag_id"]
        ).distinct()




class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create"]:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(request.method)

class NewsLetterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsLetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create"]:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)




class CommentViewSet(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, post_id, *args, **kwargs):
        comment = Comment.objects.filter(post=post_id).order_by("-created_at")
        if not comment.exists():
            return Response({"message": "Comment is zero"}, status=status.HTTP_200_OK)
        serializer_data = CommentSerializer(comment, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request, post_id, *args, **kwargs):
        request.data.update({"post": post_id})
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except:
            return Response(
                {"error": "Comment Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CommentSerializer(
            comment,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except:
            return Response(
                {"error": "Comment Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
        comment.delete()
        return Response(
            {"message": "Comment deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
    permission_classes = [permissions.AllowAny]
