from django.shortcuts import render
from .models import Services, Post, Project, Staff, MetaData
import datetime


def homepage(request):
    services = Services.objects.all()
    services_ = Services.objects.filter(id__lte=4)
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "index.html",
        {"services": services, "services_": services_, "metadata": metadata},
    )


def aboutUsPage(request):
    services = Services.objects.all()
    staffs = Staff.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "about.html",
        {"services": services, "staffs": staffs, "metadata": metadata},
    )


def servicePage(request):
    services = Services.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request, "services.html", {"services": services, "metadata": metadata}
    )


def serviceDetailsPage(request, id):
    service = Services.objects.get(id=id)
    services = Services.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "services-detail.html",
        {"services": services, "s": service, "metadata": metadata},
    )


def newsPage(request):
    services = Services.objects.all()
    posts = Post.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "news.html",
        {"posts": posts, "services": services, "metadata": metadata},
    )


def newsDetailsPage(request, id):
    post = Post.objects.get(id=id)
    services = Services.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "news-details.html",
        {"post": post, "services": services, "metadata": metadata},
    )


def projectPage(request):
    years = [year for year in range(2019, 2025)]
    services = Services.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "project.html",
        {"services": services, "years": years, "metadata": metadata},
    )


def projectDetail(request, year):
    services = Services.objects.all()
    projects = Project.objects.filter(year=year)
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "project-detail.html",
        {
            "services": services,
            "projects": projects,
            "year": year,
            "metadata": metadata,
        },
    )


def singleProjectDetail(request, id):
    project = Project.objects.get(id=id)
    services = Services.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(
        request,
        "project-detail-one.html",
        {"project": project, "services": services, "metadata": metadata},
    )


def contactPage(request):
    services = Services.objects.all()
    metadata = MetaData.objects.get(id=1)
    return render(request, "contact.html", {"metadata": metadata, "services": services})
