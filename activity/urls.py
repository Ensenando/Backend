"""
URL mapping for the user API.
"""
from django.urls import path

from activity import views

app_name = "activity"

urlpatterns = [
    path("create/lesson/<int:id>/", views.ActivityView.as_view(), name="create"),
    path("update/<int:pk>/", views.ActivityUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.ActivityDeleteView.as_view(), name="delete"),
    path("list/lesson/<int:id>/", views.ActivityListView.as_view(), name="list"),
]