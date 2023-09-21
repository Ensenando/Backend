"""
URL mapping for the user API.
"""
from django.urls import path

from dictionary import views

app_name = "dictionary"

urlpatterns = [
    path("create/", views.DictionaryView.as_view(), name="create"),
    path("update/<int:pk>/", views.DictionaryUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.DictionaryDeleteView.as_view(), name="delete"),
    path("list/", views.DictionaryListView.as_view(), name="list"),
]