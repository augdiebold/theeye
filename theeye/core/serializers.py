from django.utils import timezone

from .models import Event, ErrorLog
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    @staticmethod
    def validate_timestamp(value):
        if value > timezone.now():
            raise serializers.ValidationError("Timestamp cannot be in the future")

        return value


class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'
