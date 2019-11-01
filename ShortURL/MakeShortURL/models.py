from django.db import models
from datetime import datetime
from django.utils import timezone
class SandFURL(models.Model):
    username = models.TextField(default = None)
    FURL = models.TextField(default = None)
    SURL = models.TextField(default = None)
    howlongUsed = models.IntegerField(default = 0)
    date = models.DateTimeField(default=timezone.now(), blank=True)
    def __str__(self):
        return self.FURL
# Create your models here.
