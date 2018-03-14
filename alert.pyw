import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time

app = QApplication(sys.argv)
try:
	due = QTime.currentTime()
	message = "ALERT"

	if(len(sys.argv)<2):
		raise ValueError
	elif(len(sys.argv)>2):
		message = " ".join(sys.argv[2:])
	
	hours,mins = sys.argv[1].split(":")
	due = QTime(int(hours),int(mins))

	if not due.isValid():
		raise ValueError

except Exception:
	message = "ERROR: %s HH:MM" %(sys.argv[0].pop(1))

while QTime.currentTime()<due:
	time.sleep(20)

label = QLabel("<font size=72 color=red>%s</font>" %(message) )
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000,app.quit)

app.exec_()