from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from App.models import Lesson
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id","name","description","image","progress"]
        read_only_fields = ["id",]
                


    
        