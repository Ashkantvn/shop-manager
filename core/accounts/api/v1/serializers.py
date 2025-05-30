from rest_framework import serializers
from accounts.models import WorkingTime




class WorkingTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for working time.
    """
    class Meta:
        model = WorkingTime
        fields = ['start_time', 'end_time']
        read_only_fields = ['id']


    def create(self, validated_data):
        """
        Create a new working time instance.
        """
        return WorkingTime.objects.create(**validated_data)


    def validate(self, attrs):
        """
        Validate that start_time is before end_time.
        """
        if attrs['start_time'] >= attrs['end_time']:
            raise serializers.ValidationError("Start time must be before end time.")
        return attrs