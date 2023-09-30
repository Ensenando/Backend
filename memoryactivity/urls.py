"""
URL mapping for the user API.
"""
from django.urls import path

from memoryactivity import views

app_name = "memoryactivity"

urlpatterns = [
    path("create/activity/<int:id>/", views.MemoryActivityView.as_view(), name="create"),
    path("update/<int:pk>/", views.MemoryActivityUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.MemoryActivityDeleteView.as_view(), name="delete"),
    path("list/activity/<int:id>/", views.MemoryActivityListView.as_view(), name="list"),
]