"""
URL mapping for the user API.
"""
from django.urls import path

from secuenceactivity import views

app_name = "secuenceactivity"

urlpatterns = [
    path("create/activity/<int:id>/", views.SecuenceActivityView.as_view(), name="create"),
    path("update/<int:pk>/", views.SecuenceActivityUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.SecuenceActivityDeleteView.as_view(), name="delete"),
    path("list/activity/<int:id>/", views.SecuenceActivityListView.as_view(), name="list"),
]