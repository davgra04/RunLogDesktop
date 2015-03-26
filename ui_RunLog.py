# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_RunLog.ui'
#
# Created: Thu Mar 26 00:55:31 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runTableView = QtGui.QTableView(self.centralwidget)
        self.runTableView.setAlternatingRowColors(True)
        self.runTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.runTableView.setShowGrid(False)
        self.runTableView.setGridStyle(QtCore.Qt.SolidLine)
        self.runTableView.setSortingEnabled(True)
        self.runTableView.setWordWrap(False)
        self.runTableView.setObjectName(_fromUtf8("runTableView"))
        self.horizontalLayout.addWidget(self.runTableView)
        self.summaryBrowser = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryBrowser.sizePolicy().hasHeightForWidth())
        self.summaryBrowser.setSizePolicy(sizePolicy)
        self.summaryBrowser.setObjectName(_fromUtf8("summaryBrowser"))
        self.horizontalLayout.addWidget(self.summaryBrowser)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(True)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/appbar.refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/appbar.settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionToggle_Sidebar = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/appbar.layout.collapse.right.variant.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionToggle_Sidebar.setIcon(icon2)
        self.actionToggle_Sidebar.setObjectName(_fromUtf8("actionToggle_Sidebar"))
        self.actionAddRun = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/appbar.add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddRun.setIcon(icon3)
        self.actionAddRun.setObjectName(_fromUtf8("actionAddRun"))
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionAddRun)
        self.toolBar.addAction(self.actionToggle_Sidebar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh", None))
        self.actionRefresh.setToolTip(_translate("MainWindow", "Refresh data in table.", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionSettings.setToolTip(_translate("MainWindow", "Manage settings.", None))
        self.actionToggle_Sidebar.setText(_translate("MainWindow", "Toggle Sidebar", None))
        self.actionToggle_Sidebar.setToolTip(_translate("MainWindow", "Expands or collapses sidebar.", None))
        self.actionAddRun.setText(_translate("MainWindow", "Add Run", None))
        self.actionAddRun.setToolTip(_translate("MainWindow", "Adds a new entry into the RunLog.", None))

import icons_runlog_rc
