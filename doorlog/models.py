from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class DoorStatus(models.Model):
    UNKNOWN = "unknown"
    OPEN = "open"
    CLOSE = "close"

    doorStatus = [
        (UNKNOWN, 'unknown'),
        (OPEN, 'open'),
        (CLOSE, 'close')
    ]

    status = models.CharField(max_length=255, choices=doorStatus, default=UNKNOWN)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
