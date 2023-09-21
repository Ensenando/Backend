from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from App.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self , attr):
        data = super().validate(attr)
        token = self.get_token(self.user)
        data['user'] = str(self.user)
        data['id'] = self.user.id
        userprofileobj = get_object_or_404(User, email=self.user)
        data['role'] = userprofileobj.role
        print(userprofileobj.role)
        return data

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["id","names","surnames","email","nationality","date_of_birth","role","password"]
        read_only_fields = ["id",]

class UserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ["id", "names", "surnames", "email", "nationality", "date_of_birth", "role", "password"]
        read_only_fields = ["id", "role"]

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        
        # Remove the password field for non-PATCH operations.
        if self.context.get('request') and self.context['request'].method != 'PATCH':
            self.fields.pop('password', None)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)  # This will handle hashing the password
            user.save()

        return user   
                


    
        