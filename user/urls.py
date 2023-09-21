"""
URL mapping for the user API.
"""
from django.urls import path

from user import views

from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView,
)

app_name = "user"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("me/", views.ManageUserView.as_view(), name="me"),
]