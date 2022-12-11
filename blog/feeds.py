from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestEntriesFeed(Feed):
    title = "Django Blog latest posts"
    link = "/rssfeed"
    description = "Have the latests updates directly to your feed."

    def items(self):
        return Post.objects.filter(is_published=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:30]

    def item_link(self, item):
        return reverse('blog:detail', args=[item.slug])
