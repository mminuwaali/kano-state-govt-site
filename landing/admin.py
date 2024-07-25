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
    list_display = ["name", "sector", "created_at", "updated_at"]
