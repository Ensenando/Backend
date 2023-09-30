"""
URL mapping for the user API.
"""
from django.urls import path

from recognitionactivity import views

app_name = "recognitionactivity"

urlpatterns = [
    path("create/activity/<int:id>/", views.RecognitionActivityView.as_view(), name="create"),
    path("update/<int:pk>/", views.RecognitionActivityUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.RecognitionActivityDeleteView.as_view(), name="delete"),
    path("list/activity/<int:id>/", views.RecognitionActivityListView.as_view(), name="list"),
]