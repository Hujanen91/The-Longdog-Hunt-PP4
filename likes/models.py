from django.db import models
from blog.models import Post
from django.contrib.auth.models import User


# Create your models here.
class Like(models.Model):
    liked_posts = models.ManyToManyField(
        Post, related_name='liked_posts', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)