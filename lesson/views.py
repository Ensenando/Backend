from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from App.models import Lesson
from .serializers import (
    LessonSerializer
) 


class LessonView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny]

class LessonUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny]

    queryset = Lesson.objects.all()

class LessonDeleteView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny]

    queryset = Lesson.objects.all()


class LessonListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny]

    queryset = Lesson.objects.all()


