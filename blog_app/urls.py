from django.urls import path
from blog_app import views

app_name = "news_admin"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("post-create/", views.PostCreateView.as_view(), name="post_create"),
    path("post-detail/<int:id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post-delete/<int:id>/", views.PostDeleteView.as_view(), name="post_delete"),
    path("post-update/<int:id>/", views.PostUpdateView.as_view(), name="post_update"),


    path("draft-list/", views.DraftListView.as_view(), name="draft_list"),
    path("draft-detail/<int:id>/", views.DraftDetailView.as_view(), name="draft_detail"),
    path("draft-publish/<int:id>/", views.DraftPublishView.as_view(), name="draft_publish"),

    path('register/', views.RegisterView.as_view(), name='register'),
]
