"""
URL mapping for the user API.
"""
from django.urls import path

from resource import views

app_name = "resource"

urlpatterns = [
    path("create/activity/<int:id>/", views.ResourceView.as_view(), name="create"),
    path("update/<int:pk>/", views.ResourceUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.ResourceDeleteView.as_view(), name="delete"),
    path("list/activity/<int:id>/", views.ResourceListView.as_view(), name="list"),
]