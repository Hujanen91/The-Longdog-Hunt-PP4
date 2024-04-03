from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Like


def user_likes(request):
    # Retrieve liked posts associated with the current user
    liked_posts = request.user.liked_posts.all()
    return render(request, "liked_posts.html", {"liked_posts": liked_posts})
