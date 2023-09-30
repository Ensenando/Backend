from App.models import SecuenceActivity
from rest_framework import serializers


class SecuenceActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecuenceActivity
        fields = ["id","imageReference","image1","image2","image3","image4","image5",]
        read_only_fields = ["id",]
