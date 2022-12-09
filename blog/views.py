from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.db.models import F


def home(request):
    posts = Post.objects.select_related('author').filter(is_published=True)
    return render(request, 'blog/home.html', {'posts': posts})


def detail(request, slug):
    post = get_object_or_404(
        Post.objects.select_related('author',), slug=slug, is_published=True
    )
    post.counted_views = F('counted_views') + 1
    post.save()
    post.refresh_from_db()
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(is_published=True)
    return render(request, 'blog/home.html', {'posts': posts})


def search(request):
    query = request.GET.get('q', None)
    if query:
        posts = Post.objects.filter(content__icontains=query)
        return render(request, 'blog/home.html', {'posts': posts})
    return redirect('blog:home')
