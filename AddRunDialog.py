from __future__ import print_function
from PyQt4 import QtGui, QtCore, uic
from datetime import date
from ui_AddRunDialog import Ui_Dialog
import sys, pprint

# The QDialog presented to the user for adding new runs to the database
class AddRunDialog(QtGui.QDialog, Ui_Dialog):

    def __init__(self, parent = None):
        super(AddRunDialog, self).__init__(parent)
        self.setupUi(self)

        # Set up Calendar date selector
        self.editCalendarDate.setGridVisible(True)
        self.editCalendarDate.clicked[QtCore.QDate].connect(self.showDate)
        self.showDate(QtCore.QDate.currentDate())

        # OK and Cancel buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # Connect handlers for the seconds QSpinBoxes for run/rest
        self.connect(self.editRunSeconds, QtCore.SIGNAL('valueChanged(int)'), self.runTimeUpdated)
        self.connect(self.editRestSeconds, QtCore.SIGNAL('valueChanged(int)'), self.restTimeUpdated)


    def runTimeUpdated(self, value):
        # print('Run Time Updated!! (' + str(value) + ')')
        if value == -1:
            if self.editRunMinutes.value() != 0:                        # Decremented past minute
                self.editRunSeconds.setValue(59)
                self.editRunMinutes.setValue(self.editRunMinutes.value()-1)
                # print('Decremented past minute!')
            else:                                                       # Couldn't decrement
                self.editRunSeconds.setValue(0)
                # print('Couldn\'t decrement!')

        elif value == 60:                                               # Incremented past minute
            self.editRunSeconds.setValue(0)
            self.editRunMinutes.setValue(self.editRunMinutes.value()+1)
            # print('Incremented past minute!')


    def restTimeUpdated(self, value):
        # print('Rest Time Updated!! (' + str(value) + ')')
        if value == -1:
            if self.editRestMinutes.value() != 0:                        # Decremented past minute
                self.editRestSeconds.setValue(59)
                self.editRestMinutes.setValue(self.editRestMinutes.value()-1)
                # print('Decremented past minute!')
            else:                                                       # Couldn't decrement
                self.editRestSeconds.setValue(0)
                # print('Couldn\'t decrement!')

        elif value == 60:                                               # Incremented past minute
            self.editRestSeconds.setValue(0)
            self.editRestMinutes.setValue(self.editRunMinutes.value()+1)
            # print('Incremented past minute!')


    def showDate(self, date):
        self.editCalendarOutput.setText(date.toString())


    # get the date from the dialog
    def date(self):
        return self.editCalendarDate.selectedDate()


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

