from flask import Flask, request, Response
import json
import logging
import MySQLdb 
import re
import tweepy 


app = Flask(__name__)


def connect(db="mydb"):
	db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
	cursor = db.cursor()
	return db, cursor


def format_result(result):
	'''
	Takes cursor result, reformats to JSON
	Assumes >1 row returned
	'''
	tasks = []
	for row in result:
		data = {}
		data['question_id'] = row[0]
		data['question'] = row[1]
		data['difficulty'] = row[2]
		data['is_completed'] = row[3]
		tasks.append(data)
	return tasks



def send_tweet(question_no):
  
	# Adding necesssary keys
	consumer_key ="9B4yWmBWEo3wa2iZ3NoSvwUgF"
	consumer_secret ="JPqH0f17IraRvrtLn1HGSSqnU9NruVbp2dCtoy60FvBySPySeQ"
	access_token ="1121820237500829696-g4R2e8gpkWIL6FsHK97mgHtZploKDK"
	access_token_secret ="B4bVJSEtcPyGGV9ierSqzLMA53mymYbVytRBgmlJ0qqMx"
	  
	# Authenticating consumer key and secret 
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
	  
	# Authenticating access token and secret
	auth.set_access_token(access_token, access_token_secret) 
	api = tweepy.API(auth) 
	  
	# Posting the tweet
	api.update_status(status="Just completed SQL practice problem number {}".format(str(question_no)))




@app.route('/questions', methods=["GET"])
def show_questions():
	"""
	Show a user all questions           
	"""


	db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
	cursor = db.cursor()
	answer = cursor.execute("SELECT * FROM questions")
	answer_table = cursor.fetchall()


	formatted_answers = format_result(answer_table)
	data = {"Questions": formatted_answers}
	resp = Response(json.dumps(data), mimetype='application/json', status=200)
	return resp






@app.route('/answer', methods=["POST"])
def answer():
	"""
	Takes user the input and lets them select/answer a question   
	"""


	question_id = request.json["question_id"] 
	user_query = request.json["user_query"]
	is_correct = False


	db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
	cursor = db.cursor()
	user_result = cursor.execute(user_query)

	# Error handling for results with no rows 
	if cursor.rowcount == 0:
		data = {"Is correct": is_correct, "Problem": "No rows returned"}
		resp = Response(json.dumps(data), mimetype='application/json', status=200)
		return resp


	user_full_table = cursor.fetchall()[0][0]



	correct_query_command = cursor.execute("SELECT correct_query FROM answers WHERE question_id = %s", (int(question_id),))
	correct_query = cursor.fetchall()[0][0]
	correct_result = cursor.execute(correct_query)
	correct_full_table = cursor.fetchall()[0][0]



	# Checking to see if the answers are equal 
	if user_full_table == correct_full_table:
		is_correct = True
		send_tweet(question_id)  



	# Updating the completion status table
	sql = "UPDATE questions SET completed = %s WHERE id = %s"
	args = ("true", int(question_id))
	cursor.execute(sql, args)
	db.commit()
	db.close()




	data = {"User answer": user_full_table, "Correct answer": correct_full_table, "Is correct": is_correct}
	resp = Response(json.dumps(data), mimetype='application/json', status=200)
	return resp


