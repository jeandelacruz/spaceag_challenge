from rest_framework import serializers
from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'first_name', 'last_name', 'function']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'function': {'required': False},
        }
