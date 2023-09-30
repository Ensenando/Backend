"""
URL mapping for the user API.
"""
from django.urls import path

from theoryactivity import views

app_name = "theoryactivity"

urlpatterns = [
    path("create/activity/<int:id>/", views.TheoryActivityView.as_view(), name="create"),
    path("update/<int:pk>/", views.TheoryActivityUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.TheoryActivityDeleteView.as_view(), name="delete"),
    path("list/activity/<int:id>/", views.TheoryActivityListView.as_view(), name="list"),
]