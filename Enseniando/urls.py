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
    path("useraudit/", include("useraudit.urls"), name="useraudit"),
    path("lesson/", include("lesson.urls"), name="lesson"),
    path("userlesson/", include("userlesson.urls"), name="userlesson"),
    path("activity/", include("activity.urls"), name="activity"),
    path("score/", include("score.urls"), name="score"),
    path("goal/", include("goal.urls"), name="goal"),
    path("avatar/", include("avatar.urls"), name="avatar"),
    path('notification/', include('notification.urls'), name='notification'),
    path("notificationuser/", include("notificationuser.urls"), name="notificationuser"),
    path('certificate/', include('certificate.urls'), name='certificate'),
    path('tutorial/', include('tutorial.urls'), name='tutorial'),
    path('medal/', include('medal.urls'), name='medal'),
    path('theoryactivity/', include('theoryactivity.urls'), name='theoryactivity'),
    path('recognitionactivity/', include('recognitionactivity.urls'), name='recognitionactivity'),
    path('linkactivity/', include('linkactivity.urls'), name='linkactivity'),
    path('memoryactivity/', include('memoryactivity.urls'), name='memoryactivity'),
    path('secuenceactivity/', include('secuenceactivity.urls'), name='secuenceactivity'),
]
