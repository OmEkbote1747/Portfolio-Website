from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.contrib import messages


def home(request):

    return render(request,"home.html")


def about(request):
    return render(request, "about.html")


def skills(request):

    skills = Skill.objects.all()

    return render(
        request,
        "skills.html",
        {
            "skills": skills
        }
    )


def projects(request):

    projects = Project.objects.all()

    return render(
        request,
        "projects.html",
        {
            "projects": projects
        }
    )

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    return render(
        request,
        "project_detail.html",
        {
            "project": project
        }
    )


def journey(request):

    journey_items = Journey.objects.all()

    return render(
        request,
        "journey.html",
        {
            "journey_items": journey_items
        }
    )


def certificates(request):

    certificates = Certificate.objects.all()

    return render(
        request,
        "certificates.html",
        {
            "certificates": certificates
        }
    )


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Your message has been sent successfully."

            )

            form = ContactForm()

    else:

        form = ContactForm()

    return render(

        request,

        "contact.html",

        {

            "form": form

        }

    )