from django.shortcuts import render
from .models import Services, Post


def homepage(request):
    services = Services.objects.all()
    return render(request, "index.html", {"services": services})


def aboutUsPage(request):
    return render(request, "about.html")


def servicePage(request):
    return render(request, "services.html")


def serviceDetailsPage(request):
    return render(request, "services-detail.html")


def newsPage(request):
    posts = Post.objects.all()
    return render(request, "news.html", {"posts": posts})


def newsDetailsPage(request, id):
    post = Post.objects.get(id=id)
    return render(request, "news-details.html", {"post": post})


def projectPage(request):
    return render(request, "project.html")


def projectDetail(request):
    return render(request, "project-detail.html")
