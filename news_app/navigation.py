from news_app.models import Post, Category, Tag
from django.db.models import Sum, Count

def navigation(request):
    categories = Category.objects.all()[:4]
    tags = Tag.objects.all()[:10]

    trending_posts = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-view_count")[:4]
    

    popular_categories = Category.objects.annotate(
        total_views=Sum("posts__view_count")
    ).order_by("-total_views")[:10]   

    popular_tags = Tag.objects.annotate(
        post_count=Count("posts")      
    ).order_by("-post_count")[:10]

    random_posts = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("?")[:6]

    return {
        "categories": categories,
        "trending_posts": trending_posts,
        "tags": tags,
        "popular_categories": popular_categories,
        "popular_tags": popular_tags,
        "random_posts": random_posts,
    }
