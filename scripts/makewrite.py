#coding:utf8
import nuke
import pathapi
from PySide2.QtWidgets import *

class MakeWirte(QWidget):
	formats = ["2048x1152", "1920x1080", "2048x872"]
	exts = [".exr", ".dpx", ".jpg", ".mov"]

	def __init__(self):
	super(MakeWirte, self).__init__()
	#ok, cancel
	self.ok = QPushButton("OK")
	self.cancel = QPushButton("Cancel")
	#reformat
	self.reformat = QcheckBox(&reformat, self)
	self.reformat.setchecker(Ture)
	#fm
	self.fm = QcomboBox()
	self.fomats = ["2048x1152", "1920x1080", "2048x872"]
	self.fm.addItems(self.formats)
	#addtimecode
	self.addtimecode = QcheckBox("&AddTimecode", self)
	self.addtimcode.setChecked(False)
	#startframe, starttimecode
