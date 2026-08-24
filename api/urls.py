from django.urls import include, path
from rest_framework import routers
from api import views


router = routers.DefaultRouter()

router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"tags", views.TagViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"posts", views.PostViewSet)
router.register(r"contact", views.ContactViewSet)
router.register(r"newsletters", views.NewsLetterViewSet)


urlpatterns = [
    # Router APIs
    path("", include(router.urls)),

    # Post APIs
    path(
        "post-publish/",
        views.PostPublishViewSet.as_view(),
        name="post-publish-api",
    ),

    path(
        "draft-list/",
        views.DraftListViewSet.as_view(),
        name="draft-list-api",
    ),

    path(
        "post-by-category/<int:category_id>/",
        views.PostListByCategoryViewSet.as_view(),
        name="post-by-category-api",
    ),

    path(
        "post-by-tag/<int:tag_id>/",
        views.PostListByTagViewSet.as_view(),
        name="post-by-tag-api",
    ),

    # Comment APIs
    path(
        "post/<int:post_id>/comments/",
        views.CommentViewSet.as_view(),
        name="post-comment-api",
    ),
    path(
        "post/comments/<int:comment_id>/",
        views.CommentViewSet.as_view(),
        name="post-comment-change-api",
    ),

    # DRF login/logout
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]