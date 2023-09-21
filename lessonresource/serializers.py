from App.models import Resource
from rest_framework import serializers


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ["id","kind","url",]
        read_only_fields = ["id",]
