from rest_framework import serializers
from accounts.models import WorkingTime, BusinessWorker, BusinessManager


class WorkerSerializer(serializers.ModelSerializer):
    """
    Serializer for worker.
    """

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    manager = serializers.SerializerMethodField()

    class Meta:
        model = BusinessWorker
        fields = ["id", "first_name", "last_name", "manager"]
        read_only_fields = ["id", "first_name", "last_name", "manager"]

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
            "first_name": manager_user.first_name,
            "last_name": manager_user.last_name,
        }


# Profile serializer for manager
class WorkingTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for working time.
    """

    class Meta:
        model = WorkingTime
        fields = ["start_time", "end_time", "created_date"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        """
        Create a new working time instance.
        """
        worker = self.context.get("worker")
        validated_data["business_worker"] = worker
        return WorkingTime.objects.create(**validated_data)

    def validate(self, attrs):
        """
        Validate that start_time is before end_time.
        """
        request = self.context.get("request")
        user = request.user
        worker = self.context.get("worker")

        # Check start time is not later than end time
        if attrs["start_time"] >= attrs["end_time"]:
            raise serializers.ValidationError(
                "Start time must be before end time."
            )

        # Check manager and worker's manager are the same
        manager_of_worker = worker.business_manager
        if user.username != manager_of_worker.user.username:
            raise serializers.ValidationError(
                "Current manager and worker's manager are not same"
            )

        return attrs


class WorkerForManagerSerializer(serializers.ModelSerializer):
    """
    Serializer of workers
    for manager serializer
    """

    working_times = WorkingTimeSerializer(many=True)
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = BusinessWorker
        fields = ["id", "username", "first_name", "last_name", "working_times"]

    def get_username(self, obj):
        username = obj.user.username
        return username

    def get_first_name(self, obj):
        first_name = obj.user.first_name
        return first_name

    def get_last_name(self, obj):
        last_name = obj.user.last_name
        return last_name


class ManagerSerializer(serializers.ModelSerializer):
    """
    Serializer for manager.
    """

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    workers = WorkerForManagerSerializer(many=True)

    class Meta:
        model = BusinessManager
        fields = ["id", "first_name", "last_name", "workers"]
        read_only_fields = ["id", "first_name", "last_name", "workers"]

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
        return [
            {
                "username": worker.user.username,
                "first_name": worker.user.first_name,
                "last_name": worker.user.last_name,
                "working_time": [
                    str(time) for time in worker.working_times.all()
                ],
            }
            for worker in workers
        ]


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    access_token = serializers.CharField()
