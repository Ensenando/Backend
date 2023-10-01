from App.models import UserAudit
from rest_framework import serializers


class UserAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAudit
        fields = ["id",]
        read_only_fields = ["id",]
