from news_app.models import Post, Category, Tag

def navigation(request):

    trending_posts = Post.objects.filter(
        published_at__isnull=False, status="active"
        ).order_by("-view_count")[:3]

    categories = Category.objects.all()[:5]
    tags = Tag.objects.all()[:10]
    
    return{
        'categories' : categories, 
        'trending_posts' : trending_posts, 
        'tags' : tags,
    }
