from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    season_choices = [(None, '------')] + [(x, x) for x in range(1, 4)]
    episode_choices = [(None, '------')] + [(x, x) for x in range(1, 54)]
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    season = models.IntegerField(choices=season_choices, default=None, null=True, blank=True)
    episode = models.IntegerField(choices=episode_choices, default=None, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder', blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def number_of_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment {self.body} by {self.author}"