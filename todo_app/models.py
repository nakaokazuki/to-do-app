from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    caution = models.TextField(blank=True)
    preparation = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
