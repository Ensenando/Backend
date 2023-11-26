from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Score, Activity, User
from django.shortcuts import get_object_or_404
from .serializers import (
    ScoreSerializer
) 


class ScoreView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        activity.save()
        serializer.save(activity=Activity)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Activity created successfully'}
        return response


class ScoreUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Score.objects.all()
    

class ScoreListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return Score.objects.filter(activity=activity, user=user)


