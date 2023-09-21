from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Dictionary
from django.shortcuts import get_object_or_404
from .serializers import (
    DictionarySerializer
) 


class DictionaryView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]


class DictionaryUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Dictionary.objects.all()
        

class DictionaryDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = DictionarySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Dictionary.objects.all()
    

class DictionaryListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = DictionarySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]
    queryset = Dictionary.objects.all()


