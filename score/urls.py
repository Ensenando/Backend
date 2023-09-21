"""
URL mapping for the user API.
"""
from django.urls import path

from score import views

app_name = "score"

urlpatterns = [
    path("create/actiity/<int:id>/", views.ScoreView.as_view(), name="create"),
    path("update/<int:pk>/", views.ScoreUpdateView.as_view(), name="update"),
    path("list/activity/<int:id>/user/<int:user_id>/", views.ScoreListView.as_view(), name="list"),
]