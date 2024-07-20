from . import models
from django.shortcuts import render


def index_view(request):
    blogs = models.Blog.objects.all()

    context = {"blogs": blogs}
    return render(request, "blogging/index.html", context)


def detail_view(request, id):
    blog = models.Blog.objects.get(id=id)

    context = {"blog": blog}
    return render(request, "blogging/detail.html", context)
