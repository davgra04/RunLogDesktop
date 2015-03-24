from __future__ import print_function
from PyQt4 import QtGui, QtCore
import sys, pprint
import RunEntry, RunLogDao

class RunTableModel(QtCore.QAbstractTableModel):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.run_entries = []
        self.columns = []
        self.dao = None
        self.columns = ["run", "date", "run time", "rest time", "reps", "notes"]

    def setDatabaseInfo(self, ip, database, table, user, password):
        if self.dao:
            self.dao.setConnectionInfo(ip, database, table, user, password)
        else:
            self.dao = RunLogDao.RunLogDao(testing=False)
            self.dao.setConnectionInfo(ip, database, table, user, password)

    def refresh(self, parent=None):
        if self.dao:
            self.run_entries = self.dao.getRuns()
            # self.columns = self.dao.getColumns()
            # self.columns[0] = "run"
            self.layoutChanged.emit()

    def rowCount(self, parent=None):
        return len(self.run_entries)

    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                # return QtCore.QVariant(self.run_entries[index.row()].get_id())
                return self.rowCount()-index.row()
            if index.column() == 1:
                return QtCore.QVariant(self.run_entries[index.row()].get_date_string())
            if index.column() == 2:
                # return QtCore.QVariant(self.run_entries[index.row()].get_sec_run())
                return QtCore.QVariant( str(self.run_entries[index.row()].get_sec_run()/60) + "m " + str(self.run_entries[index.row()].get_sec_run()%60) + "s" )
            if index.column() == 3:
                # return QtCore.QVariant(self.run_entries[index.row()].get_sec_rest())
                return QtCore.QVariant( str(self.run_entries[index.row()].get_sec_rest()/60) + "m " + str(self.run_entries[index.row()].get_sec_rest()%60) + "s" )
            if index.column() == 4:
                return QtCore.QVariant(self.run_entries[index.row()].get_reps())
            if index.column() == 5:
                return QtCore.QVariant(self.run_entries[index.row()].get_note())
        return QtCore.QVariant()

    # def headerData(self, col, orientation, role):
    #     if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
    #         return QtCore.QVariant()
    #     print( "column: " + str(col) )
    #     return QtCore.QVariant(self.columns[col])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.columns[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

    def addRun(self, date, runTime, restTime, reps, note):
        print("RunTableModel:addRun")
        self.dao.addRun(date, runTime, restTime, reps, note)
        self.refresh()
        return

