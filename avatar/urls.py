"""
URL mapping for the user API.
"""
from django.urls import path

from avatar import views

app_name = "avatar"

urlpatterns = [
    path("create/user/<int:id>/", views.AvatarView.as_view(), name="create"),
    path("update/<int:pk>/", views.AvatarUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.AvatarDeleteView.as_view(), name="delete"),
    path("list/user/<int:id>/", views.AvatarListView.as_view(), name="list"),
]