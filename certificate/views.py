from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.models import Certificate, Lesson, User
from django.shortcuts import get_object_or_404
from .serializers import (
    CertificateSerializer
) 


class CertificateView(generics.CreateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        lesson.save()
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        user.save()
        serializer.save(lesson=lesson, user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'message': 'Certificate created successfully'}
        return response


class CertificateUpdateView(generics.UpdateAPIView):
    """
    View for logging in a user.
    """
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Certificate.objects.all()
        

class CertificateDeleteView(generics.DestroyAPIView):
    """
    View for logging in a user.
    """
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
    queryset = Certificate.objects.all()
    

class CertificateListView(generics.ListAPIView):
    """
    View for logging in a user.
    """
    serializer_class = CertificateSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        lesson_id = self.kwargs['id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return Certificate.objects.filter(lesson=lesson, user=user)


