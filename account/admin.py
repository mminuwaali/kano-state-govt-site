from . import models
from django.contrib import admin


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ["email"]
    search_fields = ["name", "subject", "email"]
    list_display = ["name", "email", "phone", "subject", "created_at", "updated_at"]
