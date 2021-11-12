from django.test import TestCase

from theeye.core.models import Event


class EventModelTest(TestCase):
    def setUp(self):
        self.sample_list = [
            {
                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                "category": "page interaction",
                "name": "pageview",
                "data": {
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                },
                "timestamp": "2021-01-01 09:15:27.243860"
            },
            {
                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                "category": "page interaction",
                "name": "cta click",
                "data": {
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                    "element": "chat bubble"
                },
                "timestamp": "2021-01-01 09:15:27.243860"
            },
            {
                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                "category": "form interaction",
                "name": "submit",
                "data": {
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                    "form": {
                        "first_name": "John",
                        "last_name": "Doe"
                    }
                },
                "timestamp": "2021-01-01 09:15:27.243860"
            }
        ]

        for sample in self.sample_list:
            Event.objects.create(**sample)

    def test_create(self):
        """Three Event objects should exist"""
        self.assertEqual(Event.objects.all().count(), 3)
