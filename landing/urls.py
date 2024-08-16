from . import views
from django.urls import path

app_name, urlpatterns = "landing", [
    path("", views.index_view, name="index-view"),
    path("mda/", views.mda_view, name="mda-view"),
    path("about-us/", views.about_view, name="about-view"),
    path("service/", views.service_view, name="service-view"),
    path("project/", views.project_view, name="project-view"),
    path("contact-us/", views.contact_view, name="contact-view"),
    path("government/<id>/", views.government_view, name="government-view"),
]
