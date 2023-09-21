from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Resource, Lesson
from django.shortcuts import get_object_or_404
from .serializers import (
    ResourceSerializer
) 


class ResourceView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson.save()
        serializer.save(lesson=lesson)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Resource created successfully'}
        return response


class ResourceUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Resource.objects.all()
        

class ResourceDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Resource.objects.all()
    

class ResourceListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ResourceSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return Resource.objects.filter(lesson=lesson)


