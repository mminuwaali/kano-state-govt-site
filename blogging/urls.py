from . import views
from django.urls import path

app_name,urlpatterns ="blogging", [
    path("", views.index_view, name="index-view"),
    path("<int:id>/", views.detail_view, name="detail-view"),
]
