from __future__ import print_function
from PyQt4 import QtGui, uic
import sys, pprint

form_class = uic.loadUiType("ui_SettingsDialog.ui")[0]                 # Load the UI

class SettingsDialog(QtGui.QDialog, form_class):

    def __init__(self, message = None, parent = None):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)

        if message:
            self.messageLabel.setText(message)
        else:
            self.messageLabel.hide()

        # self.ip = ""
        # self.database = ""
        # self.table = ""
        # self.user = ""
        # self.password = ""

        # OK and Cancel buttons
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    # get the ip from the dialog
    def ip(self):
        return str( self.editIP.text() )
        # return self.ip

    # get the database from the dialog
    def database(self):
        return str( self.editDatabase.text() )
        # return self.database

    # get the table from the dialog
    def table(self):
        return str( self.editTable.text() )
        # return self.table

    # get the user from the dialog
    def user(self):
        return str( self.editUser.text() )
        # return self.user

    # get the password from the dialog
    def password(self):
        return str( self.editPassword.text() )
        # return self.password

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getSettingsInfo(message = None, parent = None):
        dialog = SettingsDialog(message, parent)
        result = dialog.exec_()
        ip = dialog.ip()
        database = dialog.database()
        table = dialog.table()
        user = dialog.user()
        password = dialog.password()
        return (ip, database, table, user, password, result == QtGui.QDialog.Accepted)

