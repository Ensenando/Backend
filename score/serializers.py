from App.models import Score
from rest_framework import serializers


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id","score","name",]
        read_only_fields = ["id",]
