from django.db import models
from datetime import datetime


class Treads(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    created_time = models.DateTimeField(default=datetime.now())
