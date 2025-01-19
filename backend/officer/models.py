from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True)
    

class Officer(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name="team_members" )
    date_joined = models.DateTimeField()