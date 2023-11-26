from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Tutorial
from django.shortcuts import get_object_or_404
from .serializers import (
    TutorialSerializer
) 


class TutorialView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = TutorialSerializer
    permission_classes = [permissions.AllowAny]


class TutorialUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = TutorialSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tutorial.objects.all()
        

class TutorialDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = TutorialSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tutorial.objects.all()
    

class TutorialListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = TutorialSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tutorial.objects.all()


