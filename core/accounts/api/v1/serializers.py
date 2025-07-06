from rest_framework import serializers
from accounts.models import WorkingTime, BusinessWorker, BusinessManager




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
    

class WorkerSerializer(serializers.ModelSerializer):
    """
    Serializer for worker.
    """
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    manager = serializers.SerializerMethodField()

    class Meta:
        model = BusinessWorker
        fields = ['id', 'first_name', 'last_name', 'manager']
        read_only_fields = ['id', 'first_name', 'last_name', 'manager']

    def get_first_name(self, obj):
        """
        Get the first name of the worker.
        """
        return obj.user.first_name
    
    def get_last_name(self, obj):
        """
        Get the last name of the worker.
        """
        return obj.user.last_name

    def get_manager(self, obj):
        """
        Get the manager of the worker.
        """
        manager_user = obj.business_manager.user
        return {
            'first_name': manager_user.first_name,
            'last_name': manager_user.last_name,
        }


class ManagerSerializer(serializers.ModelSerializer):
    """
    Serializer for manager.
    """
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = BusinessManager
        fields = ['id', 'first_name', 'last_name','workers']
        read_only_fields = ['id', 'first_name', 'last_name', 'workers']

    def get_first_name(self, obj):
        """
        Get the first name of the manager.
        """
        return obj.user.first_name
    
    def get_last_name(self, obj):
        """
        Get the last name of the manager.
        """
        return obj.user.last_name
    
    def get_workers(self, obj):
        """
        Get the workers managed by the manager.
        """
        workers = obj.workers.all()
        return [{
            'username': worker.user.username,
            'first_name': worker.user.first_name,
            'last_name': worker.user.last_name,
        } for worker in workers]