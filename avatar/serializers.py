from App.models import Avatar
from rest_framework import serializers


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ["id","image",]
        read_only_fields = ["id",]
