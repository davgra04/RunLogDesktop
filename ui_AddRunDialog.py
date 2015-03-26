# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AddRunDialog.ui'
#
# Created: Thu Mar 26 22:05:17 2015
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
        Dialog.resize(402, 604)
        Dialog.setMinimumSize(QtCore.QSize(402, 604))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.editCalendarDate = QtGui.QCalendarWidget(self.groupBox)
        self.editCalendarDate.setObjectName(_fromUtf8("editCalendarDate"))
        self.gridLayout_5.addWidget(self.editCalendarDate, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.editCalendarOutput = QtGui.QLabel(self.groupBox_2)
        self.editCalendarOutput.setObjectName(_fromUtf8("editCalendarOutput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.editCalendarOutput)
        self.frame_2 = QtGui.QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.editRunMinutes = QtGui.QSpinBox(self.frame_2)
        self.editRunMinutes.setProperty("value", 1)
        self.editRunMinutes.setObjectName(_fromUtf8("editRunMinutes"))
        self.horizontalLayout.addWidget(self.editRunMinutes)
        self.editRunSeconds = QtGui.QSpinBox(self.frame_2)
        self.editRunSeconds.setMinimum(-1)
        self.editRunSeconds.setMaximum(60)
        self.editRunSeconds.setObjectName(_fromUtf8("editRunSeconds"))
        self.horizontalLayout.addWidget(self.editRunSeconds)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.frame_2)
        self.frame_3 = QtGui.QFrame(self.groupBox_2)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.editRestMinutes = QtGui.QSpinBox(self.frame_3)
        self.editRestMinutes.setProperty("value", 4)
        self.editRestMinutes.setObjectName(_fromUtf8("editRestMinutes"))
        self.horizontalLayout_3.addWidget(self.editRestMinutes)
        self.editRestSeconds = QtGui.QSpinBox(self.frame_3)
        self.editRestSeconds.setMinimum(-1)
        self.editRestSeconds.setMaximum(60)
        self.editRestSeconds.setObjectName(_fromUtf8("editRestSeconds"))
        self.horizontalLayout_3.addWidget(self.editRestSeconds)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.frame_3)
        self.editReps = QtGui.QSpinBox(self.groupBox_2)
        self.editReps.setProperty("value", 5)
        self.editReps.setObjectName(_fromUtf8("editReps"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.editReps)
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.editNote = QtGui.QTextEdit(self.groupBox_3)
        self.editNote.setObjectName(_fromUtf8("editNote"))
        self.gridLayout_2.addWidget(self.editNote, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Date", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Run Details", None))
        self.label_3.setText(_translate("Dialog", "Rest Time", None))
        self.label_4.setText(_translate("Dialog", "Reps", None))
        self.label_2.setText(_translate("Dialog", "Run Time", None))
        self.label.setText(_translate("Dialog", "Date", None))
        self.editCalendarOutput.setText(_translate("Dialog", "1/1/2000", None))
        self.editRunMinutes.setSuffix(_translate("Dialog", " min", None))
        self.editRunSeconds.setSuffix(_translate("Dialog", " sec", None))
        self.editRestMinutes.setSuffix(_translate("Dialog", " min", None))
        self.editRestSeconds.setSuffix(_translate("Dialog", " sec", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Note", None))

