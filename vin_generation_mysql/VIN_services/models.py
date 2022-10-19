from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class vinnumbers_new(models.Model):
     vinNumber= models.CharField(max_length=100, null=True)
     datetime=models.DateTimeField(default=timezone.now)