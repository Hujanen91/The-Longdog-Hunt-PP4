from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form class for creating and updating Comments.
    """
    class Meta:
        model = Comment
        fields = ('body',)
