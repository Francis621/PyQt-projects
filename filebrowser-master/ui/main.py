# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Sat Oct 20 10:16:24 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("File Browser")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        #menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        file_menu  = self.menubar.addMenu("File")
        self.ext        = file_menu.addAction("Exit")
        MainWindow.setMenuBar(self.menubar)
        #menubar end

        #toolbar
        self.tb   = self.addToolBar("File")
        self.back = QtWidgets.QAction(QtGui.QIcon("./assets/back.png"),"Back",self)
        self.open = QtWidgets.QAction(QtGui.QIcon("./assets/open.png"),"Open",self)
        self.new_file = QtWidgets.QAction(QtGui.QIcon("./assets/newfile.png"),"New File",self)
        self.new_folder = QtWidgets.QAction(QtGui.QIcon("./assets/newfolder.png"),"New Folder",self)
        self.delete = QtWidgets.QAction(QtGui.QIcon("./assets/delete.png"),"Delete File/Folder",self)
        self.symlink = QtWidgets.QAction(QtGui.QIcon("./assets/symlink.png"),"Create Symbolic Link",self)
        self.chmod = QtWidgets.QAction(QtGui.QIcon("./assets/chmod.png"),"Create Modes Of File",self)
        
        self.tb.addAction(self.open)
        self.tb.addAction(self.back)
        self.tb.addAction(self.new_file)
        self.tb.addAction(self.new_folder)
        self.tb.addAction(self.symlink)
        self.tb.addAction(self.chmod)
        self.tb.addAction(self.delete)
        
        #toolbar end 

        #status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #status bar end

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(self):
        exit()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))

