from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # ...other fields...

class Team(models.Model):
    team_name = models.CharField(max_length=255, unique=True)
    # ...other fields...

class Activity(models.Model):
    activity_id = models.CharField(max_length=255, unique=True)
    # ...other fields...

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=255, unique=True)
    # ...other fields...

class Workout(models.Model):
    workout_id = models.CharField(max_length=255, unique=True)
    # ...other fields...
