"""
URL mapping for the user API.
"""
from django.urls import path

from linkactivity import views

app_name = "linkactivity"

urlpatterns = [
    path("create/activity/<int:id>/", views.LinkActivityView.as_view(), name="create"),
    path("update/<int:pk>/", views.LinkActivityUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.LinkActivityDeleteView.as_view(), name="delete"),
    path("list/activity/<int:id>/", views.LinkActivityListView.as_view(), name="list"),
]