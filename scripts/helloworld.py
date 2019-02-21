#coding:utf8 
import os
from PySide2.QtWidgets import *

class HelloWorld(QWidget):
	def __init__(self):
		super(HelloWorld, self).__init__()
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.setSen()

	def setSen(self):
			sentence = "hello world"
			self.layout.addWidget(QLabel("%s" % sentence))

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = HelloWorld()
	try:
		customApp.show()
	except:
		pass

#w = QWidget()
#lb = QLabel()
#lb.setText("hello World")
#layout = QHBoxLayout()
#layout.addWidget(lb)
#w.setLayout(layout)
#w.shoW
