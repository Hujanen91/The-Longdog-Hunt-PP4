from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    The view to display a list
    of published blogposts
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate comment count for each post
        for post in context['post_list']:
            post.comment_count = post.comments.count()
        return context


def post_detail(request, slug):
    """
    Handles the view for every blog post and
    its details.
    Retrieves a specific post based on the
    blogposts specific slug.
    Retrieves the comments and related to
    the specific post being viewed and
    checks if the user has already liked the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.order_by("-created_on")
    comment_count = post.comments.count()
    liked = False

    if post.likes.filter(id=request.user.id).exists():
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

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "liked": liked,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


class PostLike(View):
    """
    Handles the like function on the specific
    post being viewed.
    Handles the like and dislice function
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.add_message(
                request, messages.SUCCESS,
                'You have successfully unliked this post!'
                )

        else:
            post.likes.add(request.user)
            messages.add_message(
                request, messages.SUCCESS,
                'You have successfully liked this post!'
                )
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    