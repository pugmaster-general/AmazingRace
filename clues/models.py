import datetime

from django.db import models
from django.utils import timezone

import uuid


class Clue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clue_answer = models.CharField(max_length=100, null=False, default='')
    clue_text = models.CharField(max_length=255, null=False)
    isDetour = models.BooleanField(default=False, null=False)
    showMap = models.BooleanField(default=False, null=False)
    clue_map = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.clue_answer


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(max_length=100, null=False, default='')
    jenga_score = models.IntegerField()
    volleyball_score = models.IntegerField()

    def __str__(self):
        return self.team_name