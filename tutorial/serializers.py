from App.models import Tutorial
from rest_framework import serializers


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ["id","title","description","url",]
        read_only_fields = ["id",]
