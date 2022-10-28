from unittest.util import _MAX_LENGTH
from django.db import models

class Profile(models.Model):
    slackUsername = models.CharField(max_length = 255)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.CharField()

    def __str__(self):
        return self.slackUsername
    
