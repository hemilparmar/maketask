from django.db import models
# from datetime import datetime
from django.utils import timezone

# Create your models here.
class Work(models.Model):
    sno = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    # time = models.TimeField(default=timezone.now())
    time = models.TimeField()

    def __str__(self):
        return self.name
