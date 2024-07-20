from blogging.models import Blog
from django.shortcuts import render


def index_view(request):
    blogs = Blog.objects.all()[:4]

    context = {"blogs": blogs}
    return render(request, "landing/index.html", context)


def about_view(request):
    return render(request, "landing/about.html")


def contact_view(request):
    return render(request, "landing/contact.html")


def service_view(request):
    return render(request, "landing/service.html")

def government_view(request):
    return render(request, "landing/government.html")
