from django.contrib import admin
from .models import Services, Post, Project


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
