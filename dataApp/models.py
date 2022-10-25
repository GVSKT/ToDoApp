from django.db import models
import datetime
from datetime import datetime

class ToDo(models.Model):
    try:
        username = models.CharField(max_length=300)
        task = models.CharField(max_length=300)
        status = models.CharField(max_length=300)
        status_time = models.DateTimeField(default=datetime.now())
        updation_time = models.DateTimeField(null=True)

    except Exception as ex:
        print("\nKT ... Error At Models.py ", str(ex))
