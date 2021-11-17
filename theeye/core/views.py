from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from theeye.core.filters import ErrorLogFilter, EventFilter
from theeye.core.models import Event, ErrorLog
from theeye.core.serializers import EventSerializer, ErrorLogSerializer
from theeye.core.tasks import event_handler


class EventViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter

    def create(self, request, *args, **kwargs):
        event_handler.delay(request.data)

        return Response(status=status.HTTP_202_ACCEPTED)


class ErrorLogViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer
    filterset_class = ErrorLogFilter
