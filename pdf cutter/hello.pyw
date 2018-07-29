# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyPDF2

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    saveFile = ""
    mergedFilePath = ""
    pdfFilemod = ""
    pdfFileMerge1 = ""
    pdfFileMerge2 = ""
    def __init__(self):
        self.reader = ""
        self.writter = ""
        self.merger = PyPDF2.PdfFileMerger()
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("PDF Cutter & Merger"))
        Form.resize(400, 400)
        Form.setMinimumSize(QtCore.QSize(400, 400))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        self.gridLayout_4 = QtGui.QGridLayout(Form)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.modOpenBtn = QtGui.QPushButton(self.groupBox)
        self.modOpenBtn.setObjectName(_fromUtf8("modOpenBtn"))
        self.gridLayout.addWidget(self.modOpenBtn, 0, 1, 1, 1)
        self.modField = QtGui.QLineEdit(self.groupBox)
        self.modField.setEnabled(False)
        self.modField.setObjectName(_fromUtf8("modField"))
        self.gridLayout.addWidget(self.modField, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout_2.addWidget(self.spinBox_2, 0, 2, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.modSaveBtn = QtGui.QPushButton(self.groupBox)
        self.modSaveBtn.setObjectName(_fromUtf8("modSaveBtn"))
        self.gridLayout_3.addWidget(self.modSaveBtn, 0, 0, 1, 1)
        self.modRestBtn = QtGui.QPushButton(self.groupBox)
        self.modRestBtn.setObjectName(_fromUtf8("modRestBtn"))
        self.gridLayout_3.addWidget(self.modRestBtn, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(550, 550))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.mergOpenBtn1 = QtGui.QPushButton(self.groupBox_2)
        self.mergOpenBtn1.setObjectName(_fromUtf8("mergOpenBtn1"))
        self.gridLayout_5.addWidget(self.mergOpenBtn1, 0, 1, 1, 1)
        self.mergeField1 = QtGui.QLineEdit(self.groupBox_2)
        self.mergeField1.setEnabled(False)
        self.mergeField1.setObjectName(_fromUtf8("mergeField1"))
        self.gridLayout_5.addWidget(self.mergeField1, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.mergOpenBtn1_2 = QtGui.QPushButton(self.groupBox_2)
        self.mergOpenBtn1_2.setObjectName(_fromUtf8("mergOpenBtn1_2"))
        self.gridLayout_6.addWidget(self.mergOpenBtn1_2, 0, 1, 1, 1)
        self.mergeField2 = QtGui.QLineEdit(self.groupBox_2)
        self.mergeField2.setEnabled(False)
        self.mergeField2.setObjectName(_fromUtf8("mergeField2"))
        self.gridLayout_6.addWidget(self.mergeField2, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_8.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.mergRestBtn = QtGui.QPushButton(self.groupBox_2)
        self.mergRestBtn.setObjectName(_fromUtf8("mergRestBtn"))
        self.gridLayout_8.addWidget(self.mergRestBtn, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_8)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)

        #connecting fields to files...
        self.modOpenBtn.clicked.connect(self.getModFile)
        self.modRestBtn.clicked.connect(self.resetModFields)
        self.mergOpenBtn1.clicked.connect(self.getMergFile1)
        self.mergOpenBtn1_2.clicked.connect(self.getMergeFile2)
        self.mergRestBtn.clicked.connect(self.resetMergeFields)
        self.modSaveBtn.clicked.connect(self.saveModFile)
        self.pushButton_6.clicked.connect(self.saveMergedFile)

        #Minimum
        self.spinBox.setMinimum(1)
        self.spinBox_2.setMinimum(1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def getModFile(self):
        self.pdfFilemod = str(QFileDialog.getOpenFileName()).lower()
        if(self.pdfFilemod):
	        if(self.pdfFilemod.endswith(".pdf")):
	            self.modField.setText(self.pdfFilemod)
	            self.reader = PyPDF2.PdfFileReader(self.pdfFilemod,"rb")
	            self.writter = PyPDF2.PdfFileWriter()

	            self.spinBox.setMaximum(self.reader.getNumPages())
	            self.spinBox_2.setMaximum(self.reader.getNumPages())
	        else:
	            self.showMessageBox("Error","PDF file not found.",icon=QMessageBox.Critical)
	    
    def saveModFile(self):
        minVal = min(self.spinBox.value(),self.spinBox_2.value())
        maxVal = max(self.spinBox.value(),self.spinBox_2.value())
        for num in range(0,self.reader.getNumPages()):
            if minVal-1 <= num <= maxVal-1:
                page = self.reader.getPage(num)
                self.writter.addPage(page)
        self.saveFile = str(QFileDialog.getSaveFileName()).lower()

        if(self.saveFile != ""):
            if(not self.saveFile.endswith(".pdf")):
                self.saveFile+= ".pdf"
            with open(self.saveFile,"wb") as out:
                self.writter.write(out)
            self.writter = PyPDF2.PdfFileWriter()

    def showMessageBox(self,title,data,icon=QMessageBox.Information):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(data)
        msg.exec_()

    def getMergFile1(self):
        self.pdfFileMerge1 = QFileDialog.getOpenFileName()
        self.mergeField1.setText(self.pdfFileMerge1)

    def getMergeFile2(self):
        self.pdfFileMerge2 = QFileDialog.getOpenFileName()
        self.mergeField2.setText(self.pdfFileMerge2)

    def saveMergedFile(self):
        self.merger.append(PyPDF2.PdfFileReader(file(
            self.pdfFileMerge1, 'rb')))
        self.merger.append(PyPDF2.PdfFileReader(file(
            self.pdfFileMerge2, 'rb')))
        self.mergedFilePath = str(QFileDialog.getSaveFileName()).lower()
        if(self.mergedFilePath != ""):
            if(not self.mergedFilePath.endswith(".pdf")):
                self.mergedFilePath+= ".pdf"
            self.merger.write(self.mergedFilePath)

        self.merger = PyPDF2.PdfFileMerger()

    def resetMergeFields(self):
        self.mergeField1.setText("")
        self.mergeField2.setText("")

    def resetModFields(self):
        self.modField.setText("")
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Modify PDF:", None))
        self.modOpenBtn.setText(_translate("Form", "Open File...", None))
        self.label.setText(_translate("Form", "From Page / To Page:", None))
        self.modSaveBtn.setText(_translate("Form", "Save To ...", None))
        self.modRestBtn.setText(_translate("Form", "Reset", None))
        self.groupBox_2.setTitle(_translate("Form", "Merge PDFs:", None))
        self.mergOpenBtn1.setText(_translate("Form", "Open File...", None))
        self.mergOpenBtn1_2.setText(_translate("Form", "Open File...", None))
        self.pushButton_6.setText(_translate("Form", "Merge/Save To..", None))
        self.mergRestBtn.setText(_translate("Form", "Reset", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())