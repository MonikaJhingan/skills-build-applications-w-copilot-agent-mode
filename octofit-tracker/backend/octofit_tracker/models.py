# filepath: /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/octofit_tracker/models.py
from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for compatibility with djongo
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()