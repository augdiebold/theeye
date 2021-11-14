from .models import Event, ErrorLog
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'
