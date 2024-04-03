from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
from likes.models import Like


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Custom admin configuration for managing
    Post objects in the Django admin interface.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
