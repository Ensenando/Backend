"""
URL mapping for the user API.
"""
from django.urls import path

from notification import views

app_name = "notification"

urlpatterns = [
    path("create/user/<int:id>/", views.NotificationView.as_view(), name="create"),
    path("update/<int:pk>/", views.NotificationUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.NotificationDeleteView.as_view(), name="delete"),
    path("list/user/<int:id>/", views.NotificationListView.as_view(), name="list"),
]