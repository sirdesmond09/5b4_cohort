from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    list_editable = ["status"]
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog_post', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('name', 'email', 'message')
    raw_id_fields = ('blog_post',)
