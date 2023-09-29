from App.models import Medal
from rest_framework import serializers

class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medal
        fields = ["image","description",]
        read_only_fields = ["id",]