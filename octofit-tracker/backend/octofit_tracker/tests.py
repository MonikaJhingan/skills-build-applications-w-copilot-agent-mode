from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(team_name="Team A")
        self.assertEqual(team.team_name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(activity_id="ACT123")
        self.assertEqual(activity.activity_id, "ACT123")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(leaderboard_id="LB123")
        self.assertEqual(leaderboard.leaderboard_id, "LB123")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(workout_id="WO123")
        self.assertEqual(workout.workout_id, "WO123")
