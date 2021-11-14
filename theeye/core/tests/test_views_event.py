from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.shortcuts import resolve_url as r
from theeye.core.views import EventViewSet


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

    def test_post(self):
        url = r('core:event-list')
        for sample in self.sample_list:
            response = self.client.post(url, sample, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        url = r('core:event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
