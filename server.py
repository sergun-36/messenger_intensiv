from flask import Flask, request, abort
from datetime import datetime
import time

db = [
		{
			"name": "Nick",
			"text": "Hello",
			"time": time.time()
		},
		{
			"name": "Ivan",
			"text": "Hello, Nick",
			"time": time.time()
		}]



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, messanger!"

@app.route("/status")
def status():
	data = {"time":time.time(),
			"name":"SA" ,
			"status":True,
			"time2":time.asctime(),
			"time3":datetime.now(),
			"time4": str(datetime.now()),
			"time5": datetime.now().isoformat(),
			"time6": datetime.now().strftime("%Y/%m/%d %H:%M")}
	return data

@app.route("/send", methods=["POST"])
def send_message():
	data = request.json

	if not isinstance(data, dict):
		return abort(400)

	if not data.get("name") or not data.get("text"):
		return abort(400)

	name = data["name"]
	text = data["text"]

	if not isinstance(name, str) or not isinstance(text, str):
		return abort(400)

	if 	not name or not text:
		return abort(400)



	db.append({
		"name": name,
		"text": text,
		"time": time.time() 
		})

	return {"ok": True}


@app.route("/messages")
def get_messages():
	try:
		after = float(request.args["after"])
	except:
		return abort(400)

	messages = []
	for message in db:
		if message["time"] > after:
			messages.append(message)

	return {
			"messages": messages[:50]
			}
	#data_json = json.dumps(data)
	#return jsonify(data_json)

app.run(debug='true')