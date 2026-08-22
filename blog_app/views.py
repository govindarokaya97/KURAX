from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormView

from news_app.models import Post
from .forms import PostForm, RegisterForm


class PostListView(ListView):
    model = Post
    template_name = "panel/post_list.html"
    context_object_name = "posts"
    paginate_by = 8
    
    queryset = Post.objects.filter(
        published_at__isnull=False
    ).order_by("-published_at")


class PostDetailView(DetailView):
    model = Post
    template_name = "panel/post_detail.html"
    context_object_name = "post"
    queryset = Post.objects.filter(
        published_at__isnull=False
    )
    pk_url_kwarg = "id"


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "panel/post_create.html"
    success_url = reverse_lazy("news-admin:draft_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "panel/post_create.html"
    form_class = PostForm
    pk_url_kwarg = "id"

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()

        if self.object.published_at:
            return redirect(
                "news-admin:post_detail",
                id=self.object.id,
            )

        return redirect(
            "news-admin:draft_detail",
            id=self.object.id,
        )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)

        was_published = post.published_at is not None
        post.delete()

        if was_published:
            return redirect("news-admin:post_list")

        return redirect("news-admin:draft_list")


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "panel/draft_list.html"
    context_object_name = "posts"
    queryset = Post.objects.filter(
        published_at__isnull=True
    )


class DraftDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "panel/draft_detail.html"
    context_object_name = "post"
    queryset = Post.objects.filter(
        published_at__isnull=True
    )
    pk_url_kwarg = "id"


class DraftPublishView(LoginRequiredMixin, View):
    def get(self, request, id):
        post = get_object_or_404(
            Post,
            id=id,
            published_at__isnull=True,
        )

        post.published_at = timezone.now()
        post.save(update_fields=["published_at"])

        return redirect("news-admin:post_list")


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")