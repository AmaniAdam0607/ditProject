from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.aboutUsPage, name="about"),
    path("service/", views.servicePage, name="service"),
    path("service/<int:id>", views.serviceDetailsPage, name="service_detail"),
    path("news/", views.newsPage, name="news"),
    path("news/<int:id>", views.newsDetailsPage, name="news_details"),
    path("projects/", views.projectPage, name="projects"),
    path("projects/<int:year>", views.projectDetail, name="project_detail"),
    path("projects/desc/<int:id>", views.singleProjectDetail, name="single_project"),
    path("contact/", views.contactPage, name="contact"),
]
