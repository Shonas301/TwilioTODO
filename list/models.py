import datetime
from django.db import models
from django.utils import timezone

class TODO(models.Model):
    task = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.task
    def is_due_soon(self):
        return self.due_date >= timezone.now() - datetime.timedelta(hours=2)
    def is_due_now(self):
        return self.due_date >= timezone.now() - datetime.timedelta(minutes=15)
