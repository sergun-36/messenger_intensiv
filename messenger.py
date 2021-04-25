import time
from datetime import datetime

db1 = [0]

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

def print_messages(messages):
	for message in messages:
		time_str = datetime.fromtimestamp(message["time"])
		print(message["name"], time_str)
		print(message["text"])
		print()

def send_message(name, text):
	db.append({
		"name": name,
		"text": text,
		"time": time.time() 
		})


def get_messages(after):
	messages = []
	for message in db:
		if message["time"] >= after:
			messages.append(message)

	return messages[:50]

