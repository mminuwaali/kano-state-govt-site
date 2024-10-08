from . import forms, models
from blogging.models import Blog
from django.contrib import messages
from django.shortcuts import render, redirect
from website.decorator import set_sectors_with_governance


@set_sectors_with_governance
def index_view(request):
    blogs = Blog.objects.all()[:4]

    context = {"blogs": blogs}
    return render(request, "landing/index.html", context)


@set_sectors_with_governance
def about_view(request):
    return render(request, "landing/about.html")


@set_sectors_with_governance
def mda_view(request):
    return render(request, "landing/mda.html")


@set_sectors_with_governance
def service_view(request):
    return render(request, "landing/service.html")


@set_sectors_with_governance
def project_view(request):
    projects = models.Project.objects.all()
    statuses = models.ProjectStatus.objects.all()

    filter_attr = request.GET.get("filter")

    if filter_attr:
        projects = projects.filter(status__id=int(filter_attr))

    context = {
        "projects": projects,
        "statuses": statuses,
    }
    return render(request, "landing/project.html", context)


@set_sectors_with_governance
def government_view(request, id):
    member = models.Govenance.objects.get(id=id)

    context = {"member": member}
    return render(request, "landing/government.html", context)


@set_sectors_with_governance
def contact_view(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "Something went wrong")

        return redirect("landing:contact-view")
    return render(request, "landing/contact.html")
