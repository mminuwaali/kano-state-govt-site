from . import models
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ["name", "email", "phone", "subject", "message"]
