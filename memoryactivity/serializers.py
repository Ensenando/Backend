from App.models import MemoryActivity
from rest_framework import serializers


class MemoryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryActivity
        fields = ["id","image1","image2","image3","image4","image5","pairimage1","pairimage2","pairimage3","pairimage4","pairimage5",]
        read_only_fields = ["id",]
