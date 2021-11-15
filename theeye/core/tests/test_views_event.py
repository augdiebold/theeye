from django.shortcuts import resolve_url as r
from rest_framework import status
from rest_framework.test import APITestCase

from theeye.core.models import ErrorLog


class EventViewSetTest(APITestCase):
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

        self.invalid_sample = {}

    def test_post(self):
        """POST method to api/events should return a HTTP 201 status code"""
        url = r('core:event-list')
        for sample in self.sample_list:
            response = self.client.post(url, sample, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        """GET method to api/events should return a HTTP 200 status code"""
        url = r('core:event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_post(self):
        """INVALID POST method to api/events should create an ErrorLog object"""
        url = r('core:event-list')
        self.client.post(url, self.invalid_sample, format='json')
        self.assertTrue(ErrorLog.objects.exists())