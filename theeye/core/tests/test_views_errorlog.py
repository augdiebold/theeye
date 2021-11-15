from django.shortcuts import resolve_url as r
from rest_framework import status
from rest_framework.test import APITestCase


class ErrorLogViewSetTest(APITestCase):
    def test_get(self):
        """GET method to api/errors should return a HTTP 200 status code"""
        url = r('core:errorlog-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)