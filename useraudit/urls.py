"""
URL mapping for the user API.
"""
from django.urls import path

from useraudit import views

app_name = "useraudit"

urlpatterns = [
    path("create/user/<int:user_id>/", views.UserAuditView.as_view(), name="create"),
    path("list/user/<int:user_id>", views.UserAuditListView.as_view(), name="list"),
]