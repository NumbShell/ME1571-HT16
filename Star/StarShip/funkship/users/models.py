import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    user_text = models.CharField(max_length=200)
    user_online = models.BooleanField()
    pub_date = models.DateTimeField('Date created')

    def __str__(self):
        return self.user_text

    def online(self):
        return self.user_online

    def published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    current_players = models.BigIntegerField()
    pub_date = models.DateTimeField('Date created')

    def __str__(self):
        return self.room_name

    def players(self):
        return self.current_players

    def published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)