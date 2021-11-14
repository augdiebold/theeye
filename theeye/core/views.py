from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from theeye.core.models import Event
from theeye.core.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
