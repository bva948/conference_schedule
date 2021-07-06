from django.db import models
from django.contrib.auth.models import User

class ConferenceRoom(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Tag(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Conference(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    room=models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    participants=models.ManyToManyField(User)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

