from flask import Flask, request
import json

app = Flask(__name__)

todos = {}

@app.route("/get/")
def get_all() :
	return json.dumps(todos)

@app.route("/get/<id>/")
def get_id(id) :
	return todos[int(id)]

@app.route("/done/<id>/")
def done(id) :
	i_id = int(id)
	if i_id in todos :
		todos.pop(i_id)

@app.route("/put/<id>/", methods=['PUT'])
def put(id) :
	todos[int(id)] = request.data
	return "ok"

if __name__=='__main__' :
	app.run('0.0.0.0', port=5000)
	
