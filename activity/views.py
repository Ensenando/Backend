from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Activity, Lesson
from django.shortcuts import get_object_or_404
from .serializers import (
    ActivitySerializer
) 


class ActivityView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson.save()
        serializer.save(lesson=lesson)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Activity created successfully'}
        return response


class ActivityUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Activity.objects.all()
        

class ActivityDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Activity.objects.all()
    

class ActivityListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return Activity.objects.filter(lesson=lesson)


