# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_SettingsDialog.ui'
#
# Created: Thu Mar 26 00:55:38 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(408, 249)
        Dialog.setMinimumSize(QtCore.QSize(297, 226))
        Dialog.setMaximumSize(QtCore.QSize(479, 294))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.editIP = QtGui.QLineEdit(self.frame)
        self.editIP.setObjectName(_fromUtf8("editIP"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editIP)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.editDatabase = QtGui.QLineEdit(self.frame)
        self.editDatabase.setObjectName(_fromUtf8("editDatabase"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.editDatabase)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.editUser = QtGui.QLineEdit(self.frame)
        self.editUser.setObjectName(_fromUtf8("editUser"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.editUser)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.editPassword = QtGui.QLineEdit(self.frame)
        self.editPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.editPassword.setObjectName(_fromUtf8("editPassword"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.editPassword)
        self.editTable = QtGui.QLineEdit(self.frame)
        self.editTable.setObjectName(_fromUtf8("editTable"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.editTable)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.messageLabel = QtGui.QLabel(Dialog)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.gridLayout.addWidget(self.messageLabel, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.editPassword, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.editIP)
        Dialog.setTabOrder(self.editIP, self.editDatabase)
        Dialog.setTabOrder(self.editDatabase, self.editTable)
        Dialog.setTabOrder(self.editTable, self.editUser)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Database Settings", None))
        self.label.setText(_translate("Dialog", "RunLog Database IP", None))
        self.editIP.setText(_translate("Dialog", "10.0.0.218", None))
        self.label_2.setText(_translate("Dialog", "Database", None))
        self.editDatabase.setText(_translate("Dialog", "personalDB", None))
        self.label_3.setText(_translate("Dialog", "Table", None))
        self.label_4.setText(_translate("Dialog", "User", None))
        self.editUser.setText(_translate("Dialog", "testUser", None))
        self.label_5.setText(_translate("Dialog", "Password", None))
        self.editPassword.setText(_translate("Dialog", "test123", None))
        self.editTable.setText(_translate("Dialog", "runlog_test", None))
        self.messageLabel.setText(_translate("Dialog", "Optional Label for Stuff", None))

