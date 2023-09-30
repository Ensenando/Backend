from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Activity, LinkActivity
from django.shortcuts import get_object_or_404
from .serializers import (
    LinkActivitySerializer
) 


class LinkActivityView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LinkActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        activity.save()
        serializer.save(activity=activity)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'LinkActivity created successfully'}
        return response


class LinkActivityUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LinkActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = LinkActivity.objects.all()
        

class LinkActivityDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LinkActivitySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = LinkActivity.objects.all()
    

class LinkActivityListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = LinkActivitySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        activity_id = self.kwargs['id']
        activity = get_object_or_404(Activity, id=activity_id)
        return LinkActivity.objects.filter(activity=activity)


