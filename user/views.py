from rest_framework import (
    permissions,
    generics,
    status,
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from .serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UserSerializer,
) 


class LoginView(TokenObtainPairView):
    """
    View for logging in a user.
    """
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

class CreateUserView(generics.CreateAPIView):
    """
    View for creating a user.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = request.data.get('password')
        serializer.validated_data['password'] = make_password(password)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {'message': 'User created successfully'}
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    
class ManageUserView(generics.RetrieveUpdateDestroyAPIView): # GET, PUT, PATCH
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user