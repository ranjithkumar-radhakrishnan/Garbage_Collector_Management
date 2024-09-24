import uuid
from datetime import datetime

from django.db import models


# Create your models here.


class User(models.Model):
    userId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=320, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=100, null=False)


