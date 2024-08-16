from django.db import models
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField


class Sector(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.title()


class Govenance(models.Model):
    content = MarkdownxField(default="")
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    sector = models.ForeignKey(Sector, models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def formatted_content(self):
        return markdownify(self.content)

    def __str__(self) -> str:
        return f"{self.name} - {self.sector.name}"


class ProjectStatus(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    description = MarkdownxField(default="")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(ProjectStatus, on_delete=models.PROTECT)

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def __str__(self):
        return f"{self.name} - {self.status.name}"
