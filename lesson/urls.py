"""
URL mapping for the user API.
"""
from django.urls import path

from lesson import views

app_name = "lesson"

urlpatterns = [
    path("create/", views.LessonView.as_view(), name="create"),
    path("update/<int:pk>/", views.LessonUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.LessonDeleteView.as_view(), name="delete"),
    path("list/", views.LessonListView.as_view(), name="list"),
]