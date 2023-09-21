"""
URL mapping for the user API.
"""
from django.urls import path

from goal import views

app_name = "goal"

urlpatterns = [
    path("create/user/<int:id>/", views.GoalView.as_view(), name="create"),
    path("update/<int:pk>/", views.GoalUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.GoalDeleteView.as_view(), name="delete"),
    path("list/user/<int:id>/", views.GoalListView.as_view(), name="list"),
]