from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
urlpatterns = [
    path("admin/", admin.site.urls),

    path("",include("news_app.urls")),

    path(
        "news-admin/",
        include(("blog_app.urls", "news-admin"), namespace="news-admin")
    ),

    path("api/v1/",include("api.urls")),


    path("account/login/", views.LoginView.as_view(), name="login"),
    path("account/logout/", views.LogoutView.as_view(), name="logout"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
