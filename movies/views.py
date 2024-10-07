from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie

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

    return render(
    request,
    "movies/movie_detail.html",
    {"movie": movie}, 
    
    )