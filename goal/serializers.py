from App.models import Goal
from rest_framework import serializers


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ["id","objective","status",]
        read_only_fields = ["id",]
