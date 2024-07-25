from blogging.models import Blog
from django.shortcuts import render
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
def contact_view(request):
    return render(request, "landing/contact.html")


@set_sectors_with_governance
def service_view(request):
    return render(request, "landing/service.html")


@set_sectors_with_governance
def government_view(request):
    return render(request, "landing/government.html")
