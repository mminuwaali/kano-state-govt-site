from django.db import models
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField


class Blog(models.Model):
    content = MarkdownxField(default="")
    summary = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images", blank=True, null=True)

    @property
    def formatted_content(self):
        return markdownify(self.content)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title.title()
