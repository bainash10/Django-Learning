from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #blank means can be left blanks
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated=models.DateTimeField(auto_now=True) #auto_now takes snapshot everytime
    created = models.DateTimeField(auto_now_add=True) #auto_now_add takes snapshot when we save the instance, for initial time

    class Meta:
        ordering = ['-updated', '-created']

    def  __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #cascade is used to delete all the messages if rooms get deleted
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]