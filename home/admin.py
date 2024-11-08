from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'title', 'created']
    search_fields = ('slug',)
    list_filter = ('updated',)
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('user',)
