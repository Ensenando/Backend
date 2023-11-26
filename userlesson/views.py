from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from App.models import UserLesson, Lesson, User
from django.shortcuts import get_object_or_404
from .serializers import (
    UserLessonSerializer
) 


class UserLessonView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = UserLessonSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson.save()
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        user.save()
        serializer.save(lesson=lesson, user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'UserLesson created successfully'}
        return response

class UserLessonUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = UserLessonSerializer
    permission_classes = [permissions.AllowAny]

    queryset = UserLesson.objects.all()

class UserLessonDeleteView(generics.DestroyAPIView):
    serializer_class = UserLessonSerializer
    permission_classes = [permissions.AllowAny]
    queryset = UserLesson.objects.all()


class UserLessonListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = UserLessonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return UserLesson.objects.filter(lesson=lesson, user=user)


