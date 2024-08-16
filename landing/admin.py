from . import models
from django.contrib import admin


@admin.register(models.Sector)
class SectorAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(models.Govenance)
class GovenanceAdmin(admin.ModelAdmin):
    list_filter = ["sector"]
    search_fields = ["name"]
    fields = ["sector", "name", "content"]
    list_display = ["name", "image", "sector", "created_at", "updated_at"]


@admin.register(models.ProjectStatus)
class ProjectStatusAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ["status"]
    search_fields = ["name"]
    fields = ["name", "description", "image", "status"]
    list_display = ["name", "status", "created_at", "updated_at"]
