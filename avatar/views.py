from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Avatar, User
from django.shortcuts import get_object_or_404
from .serializers import (
    AvatarSerializer
) 


class AvatarView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        user_id = self.kwargs['id']
        user = get_object_or_404(User, id=user_id)
        user.save()
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Avatar created successfully'}
        return response


class AvatarUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Avatar.objects.all()
        

class AvatarDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Avatar.objects.all()
    

class AvatarListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = AvatarSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user_id = self.kwargs['id']
        user = get_object_or_404(User, id=user_id)
        return User.objects.filter(user=user)


