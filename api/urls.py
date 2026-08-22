from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"tags", views.TagViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "post-publish/",
        views.PostPublishViewSet.as_view(),
        name="post_publish_api",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]