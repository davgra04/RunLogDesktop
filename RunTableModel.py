from __future__ import print_function
from PyQt4 import QtGui, QtCore
import sys, pprint
import RunEntry, RunLogDao

class RunTableModel(QtCore.QAbstractTableModel):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.run_entries = []
        self.columns = []

        self.dao = RunLogDao.RunLogDao(testing=False)

    def refresh(self, parent=None):
        self.run_entries = self.dao.getRuns()
        self.columns = self.dao.getColumns()
        self.layoutChanged.emit()

    def rowCount(self, parent=None):
        return len(self.run_entries)

    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return QtCore.QVariant(self.run_entries[index.row()].get_id())
            if index.column() == 1:
                return QtCore.QVariant(self.run_entries[index.row()].get_date_string())
            if index.column() == 2:
                return QtCore.QVariant(self.run_entries[index.row()].get_sec_run())
            if index.column() == 3:
                return QtCore.QVariant(self.run_entries[index.row()].get_sec_rest())
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


