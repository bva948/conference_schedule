from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields.related import ForeignKey
from django.forms import ModelForm
from django.contrib.auth.models import User

class ConferenceRoom(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Conference(models.Model):
    name=models.CharField(max_length=150)
    user=models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    room=models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    participants=models.ManyToManyField(User, blank=True, null=True)
    tags=models.ManyToManyField(Tag)
    content=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['start_time']

class RoomForm(ModelForm):
    
    class Meta:
        model=ConferenceRoom
        fields=['name', 'position']