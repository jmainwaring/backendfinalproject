from flask import Flask, request, Response
import json
import logging
import re
import MySQLdb 

app = Flask(__name__)


def connect(db="mydb"):
	db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
	cursor = db.cursor()
	return db, cursor


# Send email
MAILGUN_DOMAIN_NAME = "sandbox0b767e09f57a41219bc8f5ba9e4fc0e7.mailgun.org"
MAILGUN_API_KEY="f4c5800b65118f2a047541138a2616df-3fb021d1-db424452"

def send_email(email_recipient):

	url = 'https://api.mailgun.net/v3/{}/messages'.format(MAILGUN_DOMAIN_NAME)
	auth = ('api', MAILGUN_API_KEY)
	data = {
		'from': 'Me <mailgun@{}>'.format(MAILGUN_DOMAIN_NAME),
		'to': email_recipient,
		'subject': "Task completed",
		'text': "Congratulations on completing your task!",
	}

	response = requests.post(url, auth=auth, data=data)
	return response





@app.route('/signup', methods=["POST"])
def new_user():
	"""
	Allows a new user to signup for the service 
	"""

	username = request.json["username"]
	password = request.json["password"]
	email = request.json["email"]




	########################################
	####### Additional functionality #######
	########################################
	# Need an "if" statement to check if the email address/username is already in use



	# Adding it to the database
	db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
	cursor = db.cursor()
	cursor.execute('''INSERT INTO users (username, password, email) VALUES (%s, %s, %s)''', (username, password, email))
	db.commit()
	db.close()

	data = {"Signup status": "complete"}
	resp = Response(json.dumps(data), mimetype='application/json', status=201)
	return resp




@app.route('/signin', methods=["POST"])
def signin():
	"""
	Compares the username/password with the username/password inputted and if it's a match, logs in
	the user so he/she can track which queries have been completed      
	"""

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins




@app.route('/questions', methods=["GET"])
def show_questions():
	"""
	Show a user all questions, or a specific one, or (perhaps) all the ones they have/haven't completed           
	"""

	id = request.json["id"]
	difficulty = request.json["difficulty"]








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



	# Updating the completion status table
	sql = "UPDATE questions SET completion_status = %s WHERE question_id = %s"
	args = (True, int(question_id))
	cursor.execute(sql, args)
	db.commit()
	db.close()




	data = {"User answer": user_full_table, "Correct answer": correct_full_table, "Is correct": is_correct}
	resp = Response(json.dumps(data), mimetype='application/json', status=200)
	return resp








	# Update to "true" if it's correct 
	db.commit()




	db.close() 







	# Need something to check if answer is correct 




















# Below code is just to have some boilerplate syntax. Will eventually delete.



@app.route('/v1/tasks/<task_id>', methods=['DELETE'])
def del_task(task_id):
	'''
	Accepts DELETE, deletes the task matching the given ID if it exists
	'''
	db, cursor = connect()
	task_id = int(task_id)
	exists = id_exists(db, cursor, task_id)
	sql = "DELETE FROM tasks WHERE id = %s"
	args = (task_id, )
	cursor.execute(sql, args)
	db.commit()
	db.close()

	if exists:
		resp = Response(json.dumps(None), mimetype='application/json')
		status_code = 204
	else:
		resp = Response(json.dumps({'error': 'There is no task at that id'}), mimetype='application/json')
		status_code = 404
	return resp, status_code



















@app.route('/v1/tasks', methods=["GET"])
def return_tasks():
	"""
	Returns a specific task if a 'id' is passed in. Otherwise, it returns them all.

	Args:
		id (str): id of the task you want to return

	Returns:
		A task or list of tasks
	"""

	# Checking whether there are any args passed in (if not, just return the full list)
	if request.args:

		id = request.args.get("id")

		db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
		cursor = db.cursor()
		result = cursor.execute("SELECT * FROM tasks WHERE id = %s", (int(id),))
		row = cursor.fetchone()
		db.commit()
		db.close()


		if result:
			data = {'task': row}
			resp = Response(json.dumps(data), mimetype='application/json', status=200)
		else:
			resp = Response(json.dumps({'error': 'There is no task at that id'}), mimetype='application/json', status=404)
		return resp


	# If they don't specify a task
	db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
	cursor = db.cursor()
	result = cursor.execute("SELECT * FROM tasks")
	rows = cursor.fetchall()
	data = {'tasks': rows}
	db.commit()
	db.close()

	resp = Response(json.dumps(data), mimetype='application/json', status=200)
	return resp





@app.route('/v1/tasks', methods=["DELETE"])
def delete_tasks():
	"""
	Deletes a specific task of the 'id' passed in

	Args:
		id (str): id of the task you want to delete

	Returns:
		204 code       
	"""


	# Checking whether there are any args passed in
	if request.args:

		id = request.args.get("id")

		db = MySQLdb.connect("mysql-server", "root", "secret", "mydb")
		cursor = db.cursor()

		row_count = cursor.execute("SELECT COUNT(id) FROM tasks")

		if (int(id) > row_count) or (int(id) < 0):
			resp = Response(json.dumps({'error': 'There is no task at that id'}), mimetype='application/json', status=404)
			return resp

		else:
			result = cursor.execute("DELETE FROM tasks WHERE id = %s", (int(id),))
			db.commit()
			db.close()

		# Returning response
		data = {'Deleted task': id}
		resp = Response(json.dumps(data), mimetype='application/json', status=204)
		return resp


	else:
		resp = Response(json.dumps({'error': 'There is no task at that id'}), mimetype='application/json', status=404)
		return resp





@app.route('/v1/tasks', methods=["PUT"])
def modify_tasks():
	"""
	Modifies a specific task of the 'title' that's passed in.

	Args:
		title (str): name of the task you want to modify
		title (str): name of the title you want to modify
		is_completed (str): completion status 

	Returns:
		204 code     
	"""