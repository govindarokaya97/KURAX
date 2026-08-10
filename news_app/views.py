from django.views.generic import ListView, TemplateView
from news_app.models import Post, Category, Tag
from django.utils import timezone
from datetime import timedelta

class HomeView(ListView):
    model = Post
    template_name = "kurax/index.html"
    context_object_name = "posts"

    queryset = Post.objects.filter(
        published_at__isnull=False,
        status="active"
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = self.get_queryset()

        context["trending_top"] = posts.order_by("-view_count").first()
        context["trending_bottom"] = posts.order_by("-view_count")[1:4]
        context["recent_posts"] = posts.order_by("-published_at")[:3]

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_posts"] = self.queryset.filter(
            published_at__gte=one_week_ago
        ).order_by("-published_at")[:7]
        return context


class CategoryView(TemplateView):
    template_name = "kurax/categori.html"


class AboutView(TemplateView):
    template_name = "kurax/about.html"