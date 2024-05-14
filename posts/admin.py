from django.contrib import admin

from .models import Post, Comment

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'view_count', 'writer')

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'post', 'writer')

# accounts의 admin.py
from django.contrib import admin
from .models import User

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')
