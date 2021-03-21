import datetime

from django.db import models
from django.utils import timezone

import uuid

# Create your models here.
class Clue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clue_text = models.CharField(max_length=255, null=False)
    isDetour = models.BooleanField(default=False, null=False)
    showMap = models.BooleanField(default=False, null=False)
    def __str__(self):
        return self.clue_text