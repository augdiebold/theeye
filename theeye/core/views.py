from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from theeye.core.models import Event, ErrorLog
from theeye.core.serializers import EventSerializer, ErrorLogSerializer
from theeye.core.tasks import event_handler


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        return event_handler.delay(request.data)


class ErrorLogViewSet(ListModelMixin, GenericViewSet):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer



