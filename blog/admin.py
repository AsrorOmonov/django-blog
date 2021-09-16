from django.contrib import admin

from blog.models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['title', 'author']
    search_fields = ['title', 'author']
