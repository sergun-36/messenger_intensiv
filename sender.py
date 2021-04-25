import requests

name = input("Enter name: ")

while True:
	response = requests.post(
						"http://127.0.0.1:5000/send",
						json={"name": name, "text": input("Enter message: ")}
						)
