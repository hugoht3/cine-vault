from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie
from django.contrib import messages
from .forms import CommentForm


# Create your views here.


class HomepageMovieList(generic.ListView):
    '''
    Landing page view of all the movies 
    '''
    queryset = Movie.objects.all().filter(status=1)
    template_name = "movies/index.html"
    paginate_by = 3



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