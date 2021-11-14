from django.db import models


class Event(models.Model):
    session_id = models.CharField('session_id', max_length=100)
    category = models.CharField('category', max_length=100)
    name = models.CharField('name', max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


class ErrorLog(models.Model):
    field = models.CharField('field', max_length=100)
    code = models.CharField('code', max_length=100)
    message = models.CharField('message', max_length=255)
    input = models.TextField('input')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']