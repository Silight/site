from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_date', 'published_date')
	list_filter = ['published_date', 'created_date']
	search_fields = ['text', 'title', 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date')
    list_filter = ['created_date']
    search_fields = ['text', 'author']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
