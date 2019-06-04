# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets

class ChModDialog(QtWidgets.QDialog):

    def __init__(self,perm):
        (user,group,other) = perm
        user  = self._tostr(user)
        group = self._tostr(group)
        other = self._tostr(other)
        super(ChModDialog, self).__init__()
        self.setupUi(self)
        self._check_boxes(user,group,other)

    def _tostr(self,perm):
        perm = int(perm)
        permlist = ""
        if(perm-4 >= 0): permlist+="r"; perm-=4
        if(perm-2 >= 0): permlist+="w"; perm-=2
        if(perm-1 >= 0): permlist+="x"; perm-=1
        return permlist
    
    def _check_boxes(self,user,group,other):
        if("r" in user): self.read_user.setChecked(True)
        if("w" in user): self.write_user.setChecked(True)
        if("x" in user): self.exec_user.setChecked(True)
        if("r" in group): self.read_group.setChecked(True)
        if("w" in group): self.write_group.setChecked(True)
        if("x" in group): self.exec_group.setChecked(True)
        if("r" in other): self.read_other.setChecked(True)
        if("w" in other): self.write_other.setChecked(True)
        if("x" in other): self.exec_other.setChecked(True)

    def _get_perms(self):
        user,group,other = 0,0,0
        if(self.read_user.isChecked()):   user += 4
        if(self.write_user.isChecked()):  user += 2
        if(self.exec_user.isChecked()):   user += 1

        if(self.read_group.isChecked()):  group += 4
        if(self.write_group.isChecked()): group += 2
        if(self.exec_group.isChecked()):  group += 1

        if(self.read_other.isChecked()):  other += 4
        if(self.write_other.isChecked()): other += 2
        if(self.exec_other.isChecked()):  other += 1
        return int( "".join([str(user),str(group),str(other)]) )

    def setupUi(self, chmodailog):
        chmodailog.setObjectName("chmodailog")
        chmodailog.resize(350, 300)
        chmodailog.setMinimumSize(QtCore.QSize(350, 300))
        chmodailog.setMaximumSize(QtCore.QSize(350, 300))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(chmodailog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(chmodailog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.read_user = QtWidgets.QCheckBox(self.groupBox)
        self.read_user.setObjectName("read_user")
        self.horizontalLayout.addWidget(self.read_user)
        self.write_user = QtWidgets.QCheckBox(self.groupBox)
        self.write_user.setObjectName("write_user")
        self.horizontalLayout.addWidget(self.write_user)
        self.exec_user = QtWidgets.QCheckBox(self.groupBox)
        self.exec_user.setObjectName("exec_user")
        self.horizontalLayout.addWidget(self.exec_user)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(chmodailog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.read_group = QtWidgets.QCheckBox(self.groupBox_2)
        self.read_group.setObjectName("read_group")
        self.horizontalLayout_3.addWidget(self.read_group)
        self.write_group = QtWidgets.QCheckBox(self.groupBox_2)
        self.write_group.setObjectName("write_group")
        self.horizontalLayout_3.addWidget(self.write_group)
        self.exec_group = QtWidgets.QCheckBox(self.groupBox_2)
        self.exec_group.setObjectName("exec_group")
        self.horizontalLayout_3.addWidget(self.exec_group)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(chmodailog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.read_other = QtWidgets.QCheckBox(self.groupBox_3)
        self.read_other.setObjectName("read_other")
        self.horizontalLayout_5.addWidget(self.read_other)
        self.write_other = QtWidgets.QCheckBox(self.groupBox_3)
        self.write_other.setObjectName("write_other")
        self.horizontalLayout_5.addWidget(self.write_other)
        self.exec_other = QtWidgets.QCheckBox(self.groupBox_3)
        self.exec_other.setObjectName("exec_other")
        self.horizontalLayout_5.addWidget(self.exec_other)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(chmodailog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(chmodailog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), chmodailog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), chmodailog.reject)
        QtCore.QMetaObject.connectSlotsByName(chmodailog)

    def retranslateUi(self, chmodailog):
        chmodailog.setWindowTitle(QtWidgets.QApplication.translate("chmodailog", "Change Permissions", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("chmodailog", "User", None, -1))
        self.read_user.setText(QtWidgets.QApplication.translate("chmodailog", "Read", None, -1))
        self.write_user.setText(QtWidgets.QApplication.translate("chmodailog", "Write", None, -1))
        self.exec_user.setText(QtWidgets.QApplication.translate("chmodailog", "Execute", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("chmodailog", "Group", None, -1))
        self.read_group.setText(QtWidgets.QApplication.translate("chmodailog", "Read", None, -1))
        self.write_group.setText(QtWidgets.QApplication.translate("chmodailog", "Write", None, -1))
        self.exec_group.setText(QtWidgets.QApplication.translate("chmodailog", "Execute", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("chmodailog", "Other", None, -1))
        self.read_other.setText(QtWidgets.QApplication.translate("chmodailog", "Read", None, -1))
        self.write_other.setText(QtWidgets.QApplication.translate("chmodailog", "Write", None, -1))
        self.exec_other.setText(QtWidgets.QApplication.translate("chmodailog", "Execute", None, -1))