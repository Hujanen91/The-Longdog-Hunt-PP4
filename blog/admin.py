from django.contrib import admin
from .models import Post, Comment
from likes.models import Like
from django_summernote.admin import SummernoteModelAdmin

#class LikeInline(admin.TabularInline):
#    model = Like
#    extra = 0  # Set this to 0 to prevent additional blank inline rows

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    #inlines = [LikeInline]  # Include the LikeInline in the PostAdmin

#@admin.register(Like)
#class LikeAdmin(admin.ModelAdmin):
#    list_display = ('user', 'post', 'created_at')
#    list_filter = ('created_at',)  # Add any additional filters as needed

admin.site.register(Comment)
