from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Notification, User
from django.shortcuts import get_object_or_404
from .serializers import (
    NotificationSerializer
) 


class NotificationView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        user_id = self.kwargs['id']
        user = get_object_or_404(User, id=user_id)
        user.save()
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Notification created successfully'}
        return response


class NotificationUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Notification.objects.all()
        

class NotificationDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Notification.objects.all()
    

class NotificationListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user_id = self.kwargs['id']
        user = get_object_or_404(User, id=user_id)
        return Notification.objects.filter(user=user)


