from App.models import Certificate
from rest_framework import serializers


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id","date","title","description"]
        read_only_fields = ["id",]
