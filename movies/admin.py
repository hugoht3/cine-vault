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


# admin.site.register(MovieComment)

class MovieCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(MovieComment, MovieCommentAdmin)