from django.urls import path
from news_app.views import HomeView, AboutView, CategoryView

urlpatterns = [
      path("",HomeView.as_view(), name="home"),
      path("category/",CategoryView.as_view(), name="category"),

      path("about/",AboutView.as_view(), name="about"),

]