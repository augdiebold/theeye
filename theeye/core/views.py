from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from theeye.core.models import Event, ErrorLog
from theeye.core.serializers import EventSerializer, ErrorLogSerializer
from theeye.core.tasks import event_handler


class EventViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        event_handler.delay(request.data)

        return Response(status=status.HTTP_202_ACCEPTED)


class ErrorLogViewSet(ListModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer



