from django.shortcuts import redirect, render

from django.views.generic import ListView, TemplateView, View, DetailView
from news_app.models import Post, Category, Tag, Comment, Newsletter
from django.utils import timezone
from datetime import timedelta
from news_app.forms import ContactForm, CommentForm, NewsletterForm
from django.contrib import messages
from django.db.models import Q, Count, Sum
from django.core.paginator import Paginator, PageNotAnInteger    

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

        # Categories
        categories = (
            Category.objects
            .annotate(
                total_views=Sum("posts__view_count")
            )
            .order_by("-total_views")[:4]
        )

        for category in categories:
            category.home_posts = posts.filter(
                category=category
            ).order_by("-view_count", "-published_at")[:6]

        context["categories"] = categories

        # What's New - All
        context["whatnews_top_6"] = (
            posts
            .select_related("category")
            .order_by("-published_at")[:6]
        )
        context["trending_top"] = posts.order_by("-view_count")[:1]
        context["trending_bottom"] = posts.order_by("-view_count")[1:4]
        context["recent_posts"] = posts.order_by("-published_at")[:5]

        one_week_ago = timezone.now() - timedelta(days=7)
        context["weekly_posts"] = posts.filter(
            published_at__gte=one_week_ago
        ).order_by("-view_count")[:7]
        
        return context

class AboutView(TemplateView):
    template_name = "kurax/about.html"

class ContactView(View):
    template_name = "kurax/contact.html"

    def get(self, request):
        return render(request, self.template_name)

    
    def post(self, request):
        form = ContactForm(request.POST)
        print(request)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully submit your data", extra_tags="contact")
            return redirect("contact")
        else:
            messages.error(request, "Cannot submit your data", extra_tags="contact")
            return render(request, self.template_name, {"form":form})


class PostListView(ListView):
    model = Post
    template_name = "lists/list.html"
    context_object_name = "posts"

    paginate_by = 4

    queryset = Post.objects.filter(
        published_at__isnull = False,
        status = "active",
    ).order_by(
        "-published_at",
    )


class PostDetailView(DetailView):
    model = Post
    template_name = "details/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "id"
    paginate_by = 5

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull=False, status="active")

        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()

        obj.view_count += 1
        obj.save()

        query = self.get_queryset()
        context['pre_post'] = query.filter(id__lt=obj.id).order_by("-id").first()
        context['next_post'] = query.filter(id__gt=obj.id).order_by("id").first()

        return context

class PostByCategory(ListView):
    model = Post
    template_name = "lists/list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False, 
            status="active",
            category_id=self.kwargs["category_id"]
            ).order_by(
                "-published_at",
            )

        return query 

class PostByTag(ListView):
    model = Post
    template_name = "lists/list.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(
            published_at__isnull=False,
            status="active",
            tags__id=self.kwargs["tag_id"],
        ).order_by("-published_at")

        return query 


class CommentView(View):

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get("post")

        try:
            post = Post.objects.get(
                id=post_id,
                published_at__isnull=False,
                status="active",
            )
        except Post.DoesNotExist:
            messages.error(
                request,
                "Post not found.",
                extra_tags="comment",
            )
            return redirect("home")

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            messages.success(
                request,
                "Your comment was posted successfully.",
                extra_tags="comment",
            )

            return redirect("detail", id=post.id)

        messages.error(
            request,
            "Please correct the errors below.",
            extra_tags="comment",
        )

        return render(
            request,
            "details/detail.html",
            {
                "post": post,
                "form": form,
            }
        )

class PostSearchView(View):
    template_name = "lists/search.html"

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query")
        post_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            status="active",
            published_at__isnull=False,
        ).order_by("-published_at")
        page = request.GET.get("page", 1)
        paginate_by = 4
        paginator = Paginator(post_list, paginate_by)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)

        return render(request, self.template_name, {"query": query, "page_obj": posts})


class NewsletterView(View):

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully subscribed to newslatter", extra_tags="newsletter")

        else:
            messages.error(request, "Failed, to subscribe the Newsletter", extra_tags="newsletter")

        return redirect(request.META.get("HTTP_REFERER", "/"))