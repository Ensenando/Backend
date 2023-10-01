"""
URL mapping for the user API.
"""
from django.urls import path

from userlesson import views

app_name = "userlesson"

urlpatterns = [
    path("create/lesson/<int:id>/user/<int:user_id>/", views.UserLessonView.as_view(), name="create"),
    path("update/<int:pk>/", views.UserLessonUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.UserLessonDeleteView.as_view(), name="delete"),
    path("list/lesson/<int:id>/user/<int:user_id>", views.UserLessonListView.as_view(), name="list"),
]