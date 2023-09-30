from App.models import TheoryActivity
from rest_framework import serializers


class TheoryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TheoryActivity
        fields = ["id","image","meaning","description",]
        read_only_fields = ["id",]
