from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Resource, Activity
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
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        activity.save()
        serializer.save(activity=activity)

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
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        return Resource.objects.filter(activity=activity)


