from django.db import models
import datetime
from datetime import datetime

class ToDo(models.Model):
    username = models.CharField(max_length=300)
    task = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    status_time = models.DateTimeField(default=datetime.now())

