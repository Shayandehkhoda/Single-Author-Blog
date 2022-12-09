from django.contrib import admin, messages
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

    actions = ('publish_posts',)

    def publish_posts(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} post published", messages.SUCCESS)

    publish_posts.short_description = 'Publish selected posts'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
