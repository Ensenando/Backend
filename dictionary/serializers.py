from App.models import Dictionary
from rest_framework import serializers


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ["id","word","meaning",]
        read_only_fields = ["id",]
