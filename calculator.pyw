import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form,self).__init__(parent)
		self.browser = QTextBrowser()
		self.lineEdit = QLineEdit("Enter Your Equation.")
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineEdit)
		self.setLayout(layout)
		self.lineEdit.selectAll()
		self.lineEdit.setFocus()
		self.connect(self.lineEdit,SIGNAL("returnPressed()"),self.UpdateUi)
		self.setWindowTitle("Calculate")

	def UpdateUi(self):
		try:
			text = unicode(self.lineEdit.text())
			self.browser.append(
				"<font color=blue><b>%s</b></font> = %s" %(text,eval(text))					
			)
		except:
			self.browser.append(
				"<font color=red><b>%s</b> IS INVALID.</font>" %(text)
			)

app = QApplication(sys.argv)
form = Form()

form.show()
app.exec_()