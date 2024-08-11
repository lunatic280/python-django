from django.contrib import admin
from blog.models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
