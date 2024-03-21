from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Liked(model.Models):
#    """
#    Model for blogpost likes
#    """
#    likes = models.ManyToManyField(
#        User, related_name="liked_blogpost")
#    
#    def number_of_likes(self):
#        return self.likes.count()