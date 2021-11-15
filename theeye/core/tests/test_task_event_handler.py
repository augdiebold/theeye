from django.shortcuts import resolve_url as r
from rest_framework import status
from rest_framework.test import APITestCase

from theeye.core.models import ErrorLog, Event
from theeye.core.tasks import event_handler


class EventHandlerTaskTest(APITestCase):
    def setUp(self):
        self.valid_sample = {
                                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                                "category": "page interaction",
                                "name": "pageview",
                                "data": {
                                    "host": "www.consumeraffairs.com",
                                    "path": "/",
                                },
                                "timestamp": "2021-01-01 09:15:27.243860"
                            }

        self.invalid_sample = {}

    def test_valid(self):
        """VALID data should create Event object"""
        event_handler(self.valid_sample)
        self.assertTrue(Event.objects.exists())

    def test_invalid(self):
        """INVALID data should create an ErrorLog object"""
        event_handler(self.invalid_sample)
        self.assertTrue(ErrorLog.objects.exists())