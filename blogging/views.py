from . import models
from django.shortcuts import render
from website.decorator import set_sectors_with_governance


@set_sectors_with_governance
def index_view(request):
    blogs = models.Blog.objects.all()

    context = {"blogs": blogs}
    return render(request, "blogging/index.html", context)


@set_sectors_with_governance
def detail_view(request, id):
    blog = models.Blog.objects.get(id=id)

    context = {"blog": blog}
    return render(request, "blogging/detail.html", context)
