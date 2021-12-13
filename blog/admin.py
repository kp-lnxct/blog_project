from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post, Like
# Register your models here.


@admin.register(Post)
class post_admin(admin.ModelAdmin):
    list_display = ['title','content','date']

@admin.register(Like)
class like_display(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'user_id']