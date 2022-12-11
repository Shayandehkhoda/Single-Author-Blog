from django.db import models
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='posts/%Y/%m/%d/', null=True)
    category = models.ManyToManyField('Category', related_name='posts')
    counted_views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def next_post(self):
        try:
            next = self.get_next_by_created_at()
            while next.is_published is False:
                next = next.get_next_by_created_at()
        except self.DoesNotExist:
            next = None
        finally:
            return next

    def previous_post(self):
        try:
            previous = self.get_previous_by_created_at()
            while previous.is_published is False:
                previous = previous.get_previous_by_created_at()
        except self.DoesNotExist:
            previous = None
        finally:
            return previous

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-published_date',)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
