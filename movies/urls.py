from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomepageMovieList.as_view(), name='home'),
    path('<slug:slug>', views.movie_detail, name='movie_detail'),
       path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit,
        name='comment_edit'
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete,
        name='comment_delete'
    ),

]
