from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Activity, RecognitionActivity
from django.shortcuts import get_object_or_404
from .serializers import (
    RecognitionActivitySerializer
) 


class RecognitionActivityView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = RecognitionActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        activity.save()
        serializer.save(activity=activity)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'RecognitionActivity created successfully'}
        return response


class RecognitionActivityUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = RecognitionActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = RecognitionActivity.objects.all()
        

class RecognitionActivityDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = RecognitionActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = RecognitionActivity.objects.all()
    

class RecognitionActivityListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = RecognitionActivitySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        return RecognitionActivity.objects.filter(activity=activity)


