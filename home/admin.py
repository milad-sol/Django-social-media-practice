from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'title', 'created']
    search_fields = ('slug',)
    list_filter = ('updated',)
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created', 'is_reply']
    raw_id_fields = ('user', 'post', 'reply')
