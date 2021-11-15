import json

from celery import shared_task
from rest_framework import status
from rest_framework.response import Response

from theeye.core.models import ErrorLog
from theeye.core.serializers import EventSerializer


@shared_task
def event_handler(data):
    """This task handle the payload data, if there are any errors, an ErrorLog
    object is created.
    Otherwise, if the data is valid, an Event object is created"""

    serializer = EventSerializer(data=data)

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