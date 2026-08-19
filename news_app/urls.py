from django.urls import path

from news_app.views import (
    HomeView,
    AboutView,
    ContactView,
    PostListView,
    PostDetailView,
    PostByCategory,
    PostByTag,
    CommentView,
    PostSearchView,
    NewsletterView,
)


urlpatterns = [
    # Home
    path(
        "",
        HomeView.as_view(),
        name="home",
    ),

    # Static pages
    path(
        "about/",
        AboutView.as_view(),
        name="about",
    ),
    path(
        "contact/",
        ContactView.as_view(),
        name="contact",
    ),

    # Posts
    path(
        "post-list/",
        PostListView.as_view(),
        name="post_list",
    ),
    path(
        "detail/<int:id>/",
        PostDetailView.as_view(),
        name="detail",
    ),

    # Posts by category/tag
    path(
        "post-by-category/<int:category_id>/",
        PostByCategory.as_view(),
        name="post_by_category",
    ),
    path(
        "post-by-tag/<int:tag_id>/",
        PostByTag.as_view(),
        name="post_by_tag",
    ),

    # Comments
    path(
        "post-comment/",
        CommentView.as_view(),
        name="post_comment",
    ),

    # Search
    path(
        "post-search/",
        PostSearchView.as_view(),
        name="post_search",
    ),

    # Newsletter
    path(
        "newsletter/",
        NewsletterView.as_view(),
        name="newsletter",
    ),
]