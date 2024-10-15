from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Movie
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MovieComment
from .forms import CommentForm


# Create your views here.


class HomepageMovieList(generic.ListView):
    '''
    Landing page view of all the movies 
    '''
    queryset = Movie.objects.all().filter(status=1)
    template_name = "movies/index.html"
    paginate_by = 6



def movie_detail(request, slug):
    """
    Movie details post.
    """

    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comments = movie.comments.all().order_by("-created_on")
    comment_count = movie.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = movie
            comment.save()
            messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )


    comment_form = CommentForm()

    return render(
        request,
        "movies/movie_details.html",
        {"movie": movie,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }, 
    
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit movie comments.
    """
    if request.method == "POST":

        queryset = Movie.objects.filter(status=1)
        movie = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.username == request.user:
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment is updated.'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'An error occured while updating comment, try again.'
            )

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))



def comment_delete(request, slug, comment_id):
    """
    View to delete movie comments.
    """
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.username == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted.'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments.'
        )

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))