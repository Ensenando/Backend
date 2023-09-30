from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Activity, SecuenceActivity
from django.shortcuts import get_object_or_404
from .serializers import (
    SecuenceActivitySerializer
) 


class SecuenceActivityView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = SecuenceActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        activity.save()
        serializer.save(activity=activity)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'SecuenceActivity created successfully'}
        return response


class SecuenceActivityUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = SecuenceActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = SecuenceActivity.objects.all()
        

class SecuenceActivityDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = SecuenceActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = SecuenceActivity.objects.all()
    

class SecuenceActivityListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = SecuenceActivitySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        return SecuenceActivity.objects.filter(activity=activity)


