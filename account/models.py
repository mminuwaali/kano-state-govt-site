from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
