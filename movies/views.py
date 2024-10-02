from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.


class HomepageMovieList(generic.ListView):
    queryset = Movie.objects.all().filter(status=1)
    template_name = "movies/index.html"
    paginate_by = 3