from django.shortcuts import render
from django.views import generic
from .models import Movie

# Create your views here.


class HomepageMovieList(generic.ListView):
    model = Movie