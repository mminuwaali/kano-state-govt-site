from . import views
from django.urls import path

app_name, urlpatterns = "landing", [
    path("", views.index_view, name="index-view"),
    path("about-us/", views.about_view, name="about-view"),
    path("service/", views.service_view, name="service-view"),
    path("contact-us/", views.contact_view, name="contact-view"),
    path("government/", views.government_view, name="government-view"),
]
