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
            {"name": "Alice Johnson", "email": "alice@example.com"},
            {"name": "Bob Smith", "email": "bob@example.com"},
            {"name": "Charlie Brown", "email": "charlie@example.com"},
        ]
        for user_data in users:
            User.objects.create(**user_data)

        # Populate Teams
        teams = [
            {"name": "Team Alpha", "description": "The first team"},
            {"name": "Team Beta", "description": "The second team"},
        ]
        for team_data in teams:
            Team.objects.create(**team_data)

        # Populate Activities
        activities = [
            {"name": "Running", "calories_burned_per_minute": 10},
            {"name": "Cycling", "calories_burned_per_minute": 8},
        ]
        for activity_data in activities:
            Activity.objects.create(**activity_data)

        # Populate Leaderboard
        leaderboard_entries = [
            {"user_id": 1, "team_id": 1, "points": 100},
            {"user_id": 2, "team_id": 2, "points": 80},
        ]
        for entry in leaderboard_entries:
            Leaderboard.objects.create(**entry)

        # Populate Workouts
        workouts = [
            {"user_id": 1, "activity_id": 1, "duration_minutes": 30},
            {"user_id": 2, "activity_id": 2, "duration_minutes": 45},
        ]
        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
