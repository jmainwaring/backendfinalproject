# SQL Practice App: Backend Web Architecture Project

The SQL Practice App architecture is designed to allow individuals to replicate practice scenarios similar to HackerRank locally on their machines. We split up our project into two containers: one with all of the Flask functionality (e.g. accepting user queries) and a separate one that runs MySQL.

The overall architecture has two main endpoints:
- /questions: The endpoint functions as the screen for available questions from the SQL database setup through the init_db.py file
- /answers: The endpoint allows  users to pass the answer query to a specific question id and the database matches query results based on a "correct  query" identified by the developers in the table.
- For error handling of edge cases, we take into consideration user queries that may be syntactically correct but return no rows
- Additionally, the status of a question within the database table is updated each time we identify the user query result as correct. This update persists for the session and allows users to track their progress
- Once a question_id is correctly completed, the external API connects to Twitter to push an update tweet of the progress "Just completed SQL practice problem number x" 


# Supporting files and scripts:
- redo_app.sh: Setup docker commands
- restart.sh: Stop, delete and call startup.sh to rebuild docker containers
- startup.sh : Create network for dockers and run all initializing scripts to setup SQL container and the web app
- sendtweet.py: tweepy authentication setup
- init_db.py: Create the practice database of questions, genres, movies and answers