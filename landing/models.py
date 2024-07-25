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
    updated_at = models.DateTimeField(auto_now=True)
    sector = models.ForeignKey(Sector, models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.sector.name}"
