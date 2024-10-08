from django.contrib import admin
from .models import Movie, MovieComment
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Movie)

class MoviePostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'author')
    search_fields = ['title', 'content',]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.


admin.site.register(MovieComment)