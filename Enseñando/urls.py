"""
URL configuration for Enseñando project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [   
    path("admin/", admin.site.urls),
    path(
        "api/schema/", SpectacularAPIView.as_view(), name="api-schema"
    ),  # genera el esquema de la API
    #api/docs/
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path("user/", include("user.urls"), name="user"),
    path("lesson/", include("lesson.urls"), name="lesson"),
    path("activity/", include("activity.urls"), name="activity"),
    path("score/", include("score.urls"), name="score"),
    path("goal/", include("goal.urls"), name="goal"),
    path("resource/", include("lessonresource.urls"), name="resource"),
    path("avatar/", include("avatar.urls"), name="avatar"),
    path("dictionary/", include("dictionary.urls"), name="dictionary"),
    path('notification/', include('notification.urls'), name='notification'),
    path('certificate/', include('certificate.urls'), name='certificate'),
]
