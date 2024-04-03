from django.db import models
from blog.models import Post
from django.contrib.auth.models import User


class Like(models.Model):
    """
    This model tracks likes and what user
    that liked the post.
    """
    liked_posts = models.ManyToManyField(
        Post, related_name='liked_posts', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
