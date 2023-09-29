"""
URL mapping for the user API.
"""
from django.urls import path

from tutorial import views

app_name = "tutorial"

urlpatterns = [
    path("create/", views.TutorialView.as_view(), name="create"),
    path("update/<int:pk>/", views.TutorialUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.TutorialDeleteView.as_view(), name="delete"),
    path("list/", views.TutorialListView.as_view(), name="list"),
]