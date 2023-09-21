"""
URL mapping for the user API.
"""
from django.urls import path

from lessonresource import views

app_name = "lessonresource"

urlpatterns = [
    path("create/lesson/<int:id>/", views.ResourceView.as_view(), name="create"),
    path("update/<int:pk>/", views.ResourceUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.ResourceDeleteView.as_view(), name="delete"),
    path("list/lesson/<int:id>/", views.ResourceListView.as_view(), name="list"),
]