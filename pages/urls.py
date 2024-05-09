from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("about/", views.aboutUsPage, name="about"),
    path("service/", views.servicePage, name="service"),
    path("service/detail", views.serviceDetailsPage, name="service_detail"),
    path("news/", views.newsPage, name="news"),
    path("news/<int:id>", views.newsDetailsPage, name="news_details"),
]
