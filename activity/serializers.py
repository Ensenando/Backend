from App.models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id","name","description","flag_completed","num_by_lesson",]
        read_only_fields = ["id",]
