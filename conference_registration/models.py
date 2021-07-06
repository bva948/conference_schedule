from django.db import models

class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ConferenceRoom(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Tag(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Conference(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    room=models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    participants=models.ManyToManyField(Person)
    tags=models.ForeignKey(Tag)

    def __str__(self):
        return self.name

