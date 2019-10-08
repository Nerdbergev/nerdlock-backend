from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests


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


@receiver(post_save, sender=DoorStatus)
def my_function_post_save(sender, instance, created, **kwargs):
    headers = {"Authorization": "Token a3cce2627e7dbe00506978ed76f807ec9cfa3e52"}
    json = {"status": instance.status}
    r=requests.post('http://nerdberg.de:1337/api/doorstatus/', json=json, headers=headers)

    print(r.content)
