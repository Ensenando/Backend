from App.models import LinkActivity
from rest_framework import serializers


class LinkActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkActivity
        fields = ["id","image1","image2","image3","image4","image5","meaning1","meaning2","meaning3","meaning4","meaning5",]
        read_only_fields = ["id",]
