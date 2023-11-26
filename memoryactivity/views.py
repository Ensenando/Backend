from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Activity, MemoryActivity
from django.shortcuts import get_object_or_404
from .serializers import (
    MemoryActivitySerializer
) 


class MemoryActivityView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = MemoryActivitySerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        activity.save()
        serializer.save(activity=activity)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'MemoryActivity created successfully'}
        return response


class MemoryActivityUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = MemoryActivitySerializer
    permission_classes = [permissions.AllowAny]
    queryset = MemoryActivity.objects.all()
        

class MemoryActivityDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = MemoryActivitySerializer
    permission_classes = [permissions.AllowAny]
    queryset = MemoryActivity.objects.all()
    

class MemoryActivityListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = MemoryActivitySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        return MemoryActivity.objects.filter(activity=activity)


