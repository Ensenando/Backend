from App.models import Goal
from rest_framework import serializers


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ["id","objective","period",]
        read_only_fields = ["id",]
