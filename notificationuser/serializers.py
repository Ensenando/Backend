from App.models import NotificationUser
from rest_framework import serializers


class NotificationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationUser
        fields = ["id","status",]
        read_only_fields = ["id",]
