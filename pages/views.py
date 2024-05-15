from django.shortcuts import render
from .models import Services, Post, Project


def homepage(request):
    services = Services.objects.all()
    services_ = Services.objects.filter(id__lte=4)
    return render(request, "index.html", {"services": services, "services_": services_})


def aboutUsPage(request):
    services = Services.objects.all()
    return render(request, "about.html", {"services": services})


def servicePage(request):
    services = Services.objects.all()
    return render(request, "services.html", {"services": services})


def serviceDetailsPage(request, id):
    service = Services.objects.get(id=id)
    services = Services.objects.all()
    return render(request, "services-detail.html", {"services": services, "s": service})


def newsPage(request):
    services = Services.objects.all()
    posts = Post.objects.all()
    return render(request, "news.html", {"posts": posts, "services": services})


def newsDetailsPage(request, id):
    post = Post.objects.get(id=id)
    services = Services.objects.all()
    return render(request, "news-details.html", {"post": post, "services": services})


def projectPage(request):
    years = [year for year in range(2019, 2024)]
    services = Services.objects.all()
    return render(request, "project.html", {"services": services, "years": years})


def projectDetail(request, year):
    services = Services.objects.all()
    projects = Project.objects.filter(year=year)
    return render(
        request,
        "project-detail.html",
        {"services": services, "projects": projects, "year": year},
    )


def singleProjectDetail(request, id):
    project = Project.objects.get(id=id)
    services = Services.objects.all()
    return render(
        request, "project-detail-one.html", {"project": project, "services": services}
    )
