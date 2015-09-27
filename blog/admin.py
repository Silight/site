from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_date', 'published_date')
	list_filter = ['published_date', 'created_date']
	search_fields = ['question_text', 'title', 'author']


admin.site.register(Post, PostAdmin)
