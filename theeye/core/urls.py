from django.urls import path, include
from rest_framework import routers

from .views import EventViewSet, ErrorLogViewSet

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'errors', ErrorLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
