from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Like

# Create your views here.
def user_likes(request):
    
    likes = Like.objects.all()
    return render(
        request,
        "liked_posts.html",
        {"likes": likes},
    )