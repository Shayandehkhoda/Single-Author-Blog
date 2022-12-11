from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Post, Category
from django.db.models import F
from django.core.paginator import Paginator
from .forms import NewsletterForm
from django.contrib import messages


def home(request, pnum=1):
    posts = Post.objects.select_related('author').filter(is_published=True)
    paginator = Paginator(posts, 2)
    page_number = pnum
    posts = paginator.get_page(page_number)
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
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
        return render(request, 'blog/home.html', {'posts': posts})
    return redirect('blog:home')


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed successfully.')
    return HttpResponseRedirect('/')
