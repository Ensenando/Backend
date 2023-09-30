from App.models import RecognitionActivity
from rest_framework import serializers


class RecognitionActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognitionActivity
        fields = ["id","image","meaning",]
        read_only_fields = ["id",]
