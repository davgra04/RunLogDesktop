from __future__ import print_function
from PyQt4 import QtGui, QtCore, uic
from ui_AddRunDialog import Ui_Dialog
import sys, pprint

# form_class = uic.loadUiType("ui_AddRunDialog.ui")[0]                 # Load the UI

class AddRunDialog(QtGui.QDialog, Ui_Dialog):

    def __init__(self, parent = None):
        super(AddRunDialog, self).__init__(parent)
        self.setupUi(self)

        self.editCalendarDate.setGridVisible(True)
        self.editCalendarDate.clicked[QtCore.QDate].connect(self.showDate)

        # OK and Cancel buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def showDate(self, date):
        self.editCalendarOutput.setText(date.toString())

    # get the ip from the dialog
    def date(self):
        return self.editCalendarDate.selectedDate()
        # return self.ip

    # # get the database from the dialog
    # def database(self):
    #     return str( self.editDatabase.text() )
    #     # return self.database

    # # get the table from the dialog
    # def table(self):
    #     return str( self.editTable.text() )
    #     # return self.table

    # # get the user from the dialog
    # def user(self):
    #     return str( self.editUser.text() )
    #     # return self.user

    # # get the password from the dialog
    # def password(self):
    #     return str( self.editPassword.text() )
    #     # return self.password

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getNewRunInfo(parent = None):
        dialog = AddRunDialog(parent)
        result = dialog.exec_()
        runMin = dialog.editRunMinutes.value()
        runSec = dialog.editRunSeconds.value()
        restMin = dialog.editRestMinutes.value()
        restSec = dialog.editRestSeconds.value()
        reps = dialog.editReps.value()
        note = dialog.editNote.toPlainText()
        return (dialog.date().toString(format=QtCore.Qt.ISODate), runMin*60+runSec, restMin*60+restSec, reps, note, result == QtGui.QDialog.Accepted)

