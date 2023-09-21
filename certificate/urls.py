"""
URL mapping for the user API.
"""
from django.urls import path

from certificate import views

app_name = "certificate"

urlpatterns = [
    path("create/lesson/<int:id>/user/<int:user_id>/", views.CertificateView.as_view(), name="create"),
    path("update/<int:pk>/", views.CertificateUpdateView.as_view(), name="update"),
    path("delete/<int:id>/", views.CertificateDeleteView.as_view(), name="delete"),
    path("list/lesson/<int:id>/user/<int:user_id>", views.CertificateListView.as_view(), name="list"),
]