from django.contrib import admin
from .models import Services, Post


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
