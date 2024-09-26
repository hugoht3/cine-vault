from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomepageMovieList.as_view(), name='home'),
]