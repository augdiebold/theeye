import json

from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from theeye.core.models import Event, ErrorLog
from theeye.core.serializers import EventSerializer, ErrorLogSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)

        if not serializer.is_valid():
            for field, errors in serializer.errors.items():
                for error_detail in errors:
                    ErrorLog.objects.create(field=field,
                                            code=error_detail.code,
                                            message=error_detail.title(),
                                            input=json.dumps(serializer.data))

            return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)

        else:
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ErrorLogViewSet(ListModelMixin, GenericViewSet):
    queryset = ErrorLog.objects.all()
    serializer_class = ErrorLogSerializer



