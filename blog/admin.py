from django.contrib import admin, messages
from .models import Post, Category, Newsletter, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('trunc_title', 'thumbnail', 'category_str', 'counted_views', 'is_published', 'published_date')
    list_filter = ('is_published', 'published_date', )
    search_fields = ('title', 'content')
    sortable_by = ('is_published', 'counted_views', 'published_date',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

    actions = ('publish_posts', 'draft_posts', )

    def publish_posts(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} post published", messages.SUCCESS)

    def draft_posts(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} post drafted", messages.SUCCESS)

    publish_posts.short_description = 'Publish selected posts'
    draft_posts.short_description = 'Draft selected posts'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'subject', 'approved', 'created_at')
    list_filter = ('approved', )
    search_fields = ('name', 'email')
    sortable_by = ('post', 'created_at', 'approved', 'name')

    actions = ('approve_comment',)

    def approve_comment(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} comment approved", messages.SUCCESS)

    approve_comment.short_description = 'Approve selected comments'
