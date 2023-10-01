"""
URL mapping for the user API.
"""
from django.urls import path

from notificationuser import views

app_name = "notificationuser"

urlpatterns = [
    path("create/notification/<int:id>/user/<int:user_id>/", views.NotificationUserView.as_view(), name="create"),
    path("update/<int:pk>/", views.NotificationUserUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.NotificationUserDeleteView.as_view(), name="delete"),
    path("list/notification/<int:id>/user/<int:user_id>", views.NotificationUserListView.as_view(), name="list"),
]