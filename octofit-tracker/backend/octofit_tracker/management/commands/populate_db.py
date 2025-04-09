from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate Users
        users = [
            {"username": "alice", "email": "alice@example.com", "password": "password123"},
            {"username": "bob", "email": "bob@example.com", "password": "password123"},
        ]
        user_instances = [User.objects.create(**user_data) for user_data in users]

        # Populate Teams
        teams = [
            {"name": "Team Alpha", "members": [user_instances[0]]},
            {"name": "Team Beta", "members": [user_instances[1]]},
        ]
        for team_data in teams:
            team = Team.objects.create(name=team_data["name"], members=team_data["members"])

        # Populate Activities
        activities = [
            {"user": user_instances[0], "activity_type": "Running", "duration": 30},
            {"user": user_instances[1], "activity_type": "Cycling", "duration": 45},
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Populate Leaderboard
        leaderboard_entries = [
            {"user": user_instances[0], "score": 100},
            {"user": user_instances[1], "score": 80},
        ]
        for entry in leaderboard_entries:
            Leaderboard.objects.create(**entry)

        # Populate Workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick morning run"},
            {"name": "Evening Cycle", "description": "A relaxing evening cycle"},
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))