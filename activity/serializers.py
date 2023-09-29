from App.models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id","name","description","image","num_by_lesson","kind",]
        read_only_fields = ["id",]
