from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Profile
# Register your models here.


@admin.register(Profile)
class profile_pisctu(admin.ModelAdmin):
    list_display = ['image','user_id']