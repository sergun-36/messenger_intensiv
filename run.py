from client_ui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from datetime import datetime

class App (Ui_MainWindow, QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#to run on button click
		self.pushButton.pressed.connect(self.send_message)

		#to run by timer
		self.after = 0
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.get_messages)
		self.timer.start(1000)

	def show_messages(self, messages):
		for message in messages:
			dt = datetime.fromtimestamp(message["time"])
			time_str = dt.strftime("%Y/%m/%d %H:%M")
			str_text = f"{time_str} {message['name']}\n {message['text']}\n\n"
			self.textBrowser.append(str_text)


	def get_messages(self):
		response = requests.get(
					"http://127.0.0.1:5000/messages",
					params={"after":self.after}
					)
		messages =response.json()["messages"]
		if messages:
			self.show_messages(messages)
			self.after = messages[-1]["time"]		


	def send_message(self):
		name = self.lineEdit.text()
		text = self.textEdit.toPlainText()
		response = requests.post(
					"http://127.0.0.1:5000/send",
					json={"name": name, "text": text}
					)
		#TODO response is OK
		if response.status_code != 200:
			self.textBrowser.append(f"Message is not sent\n Check message text and Name")
			return
		self.textEdit.clear()
		

app = QtWidgets.QApplication([])
window = App()
window.show()
app.exec()