// Switch to or create the octofit_db database
 octofit_db;

// Create the users collection with a unique index on the email field
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.createIndex({ "_id": 1 }, { unique: true }); // Ensure unique ID for primary key

// Create the teams collection with a unique index on the team name
db.teams.createIndex({ "teamName": 1 }, { unique: true });

// Create the activity collection with a unique index on activity ID
db.activity.createIndex({ "activityId": 1 }, { unique: true });

// Create the leaderboard collection with a unique index on leaderboard ID
db.leaderboard.createIndex({ "leaderboardId": 1 }, { unique: true });

// Create the workouts collection with a unique index on workout ID
db.workouts.createIndex({ "workoutId": 1 }, { unique: true });

// Verify the collections

collections;