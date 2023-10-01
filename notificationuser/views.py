from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import NotificationUser, Notification, User
from django.shortcuts import get_object_or_404
from .serializers import (
    NotificationUserSerializer
) 


class NotificationUserView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationUserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        notification_id = self.kwargs['id']
        notification = get_object_or_404(Notification, id=notification_id)
        notification.save()
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        user.save()
        serializer.save(notification=notification, user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'NotificationUser created successfully'}
        return response


class NotificationUserUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationUserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = NotificationUser.objects.all()
        

class NotificationUserDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationUserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = NotificationUser.objects.all()
    

class NotificationUserListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = NotificationUserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        notification_id = self.kwargs['id']
        notification = get_object_or_404(Notification, id=notification_id)
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return NotificationUser.objects.filter(notification=notification, user=user)


