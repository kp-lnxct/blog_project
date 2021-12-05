from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post
# Register your models here.


@admin.register(Post)
class post_admin(admin.ModelAdmin):
    list_display = ['title','content','date']