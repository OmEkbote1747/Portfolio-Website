from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("journey/", views.journey, name="journey"),
    path("certificates/", views.certificates, name="certificates"),
    path("contact/", views.contact, name="contact"),
]