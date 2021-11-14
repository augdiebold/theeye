from django.test import TestCase

from theeye.core.models import ErrorLog


class ErrorLogModelTest(TestCase):
    def setUp(self):
        self.sample = {
                "field": "session_id",
                "code": "required",
                "message": "This field is required.",
                "input": "",
            }

        ErrorLog.objects.create(**self.sample)

    def test_create(self):
        """ErrorLog should be created"""
        self.assertTrue(ErrorLog.objects.exists())