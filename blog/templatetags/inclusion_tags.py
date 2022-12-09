from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag('blog/widget-latestpost.html')
def latest_post():
    latest_posts = Post.objects.filter(is_published=True)[:4]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog/widget-categories.html')
def category_list():
    categories = Category.objects.all()
    return {'categories': categories}
