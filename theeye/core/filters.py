from django_filters import rest_framework as filters

from theeye.core.models import Event, ErrorLog


class EventFilter(filters.FilterSet):
    timestamp = filters.DateTimeFromToRangeFilter(field_name='timestamp')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Event
        fields = {
            'session_id': ['exact', 'icontains'],
            'category': ['exact', 'icontains'],
            'name': ['exact', 'icontains'],
        }


class ErrorLogFilter(filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = ErrorLog
        fields = ()
