from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View, generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, PostLike
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate comment count for each post
        for post in context['post_list']:
            post.comment_count = post.comments.count()
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True

        return context
    

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment_count = post.comments.count()
    liked = False

    if request.user.is_authenticated and post.likes.filter(id=request.user.id).exists():
            liked = True
            
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted successfully'
                )
            # Redirect to avoid resubmitting form on page refresh
            return HttpResponseRedirect(request.path_info)
            
            
    else:        
        comment_form = CommentForm()
    
    # Retrieve comments only if it's a GET request
    comments = post.comments.filter(approved=True).order_by("-created_on")
    
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
    
class PostLike(View):
    """ View for handling post likes. """

    def post(self, request, slug, *args, **kwargs):
        """ Toggle the like status for the current user on the specified post """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            request.user.profile.liked_posts.remove(post)
        else:
            post.likes.add(request.user)
            request.user.profile.liked_posts.add(post)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))