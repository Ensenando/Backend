from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Goal, User
from django.shortcuts import get_object_or_404
from .serializers import (
    GoalSerializer
) 


class GoalView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = GoalSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user_id = self.kwargs['id']
        user = get_object_or_404(User, id=user_id)
        user.save()
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Goal created successfully'}
        return response


class GoalUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = GoalSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Goal.objects.all()
        

class GoalDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = GoalSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Goal.objects.all()
    

class GoalListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = GoalSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['id']
        user = get_object_or_404(User, id=user_id)
        return Goal.objects.filter(user=user)


