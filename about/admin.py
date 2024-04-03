from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


# Add Summernote fields to blogpost creation in admin
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
