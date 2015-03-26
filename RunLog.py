from __future__ import print_function
from PyQt4 import QtGui, QtCore, uic
from ui_RunLog import Ui_MainWindow
import sys, pprint
import icons_runlog_rc
import RunEntry, RunLogDao, RunTableModel, SettingsDialog, AddRunDialog

# form_class = uic.loadUiType("ui_RunLog.ui")[0]                 # Load the UI from file

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):

    console_table_printing_template = "{0:>5}  {1:>10}  {2:>11}  {3:>12}  {4:>4}  {5:103}"
    sidebar_visible = True

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # self.ui = ui_RunLog.Ui_MainWindow()
        # self.ui.setupUi(self)

        # self.dao = RunLogDao.RunLogDao(testing=False)

        self.actionRefresh.triggered.connect(self.btn_refresh_clicked)
        self.actionToggle_Sidebar.triggered.connect(self.btn_sidebar_toggle)
        self.actionSettings.triggered.connect(self.btn_settings_clicked)
        self.actionAddRun.triggered.connect(self.btn_add_run_clicked)

        self.model = RunTableModel.RunTableModel()
        self.runTableView.setModel(self.model)
    
        self.columnMinSizes = [40, 80, 80, 80, 40, 100]

        # self.btn_sidebar_toggle()   # Start with sidebar hidden

        # self.resizeEvent(None)

        QtCore.QTimer.singleShot(100, self.OnLoad)


    def OnLoad(self):
        self.btn_settings_clicked(message="Input database connection info to connect.")
        self.btn_refresh_clicked()  # Start with a refresh
        self.resizeEvent(None)


    def resizeEvent(self, event):

        col_width = self.runTableView.width()/6


        for index in range(self.model.columnCount()):
            self.runTableView.setColumnWidth(index, (col_width) if col_width < self.columnMinSizes[index] else self.columnMinSizes[index])

        # self.runTableView.setColumnWidth(0, (col_width) if col_width < 30 else 30 )
        # self.runTableView.setColumnWidth(1, (col_width) if col_width < 80 else 80 )
        # self.runTableView.setColumnWidth(2, (col_width) if col_width < 80 else 80 )
        # self.runTableView.setColumnWidth(3, (col_width) if col_width < 80 else 80 )
        # self.runTableView.setColumnWidth(4, (col_width) if col_width < 60 else 60 )
        # self.runTableView.setColumnWidth(5, (col_width) if col_width < 30 else 30 )
        self.runTableView.horizontalHeader().setStretchLastSection(True)


    def btn_refresh_clicked(self):
        print("REFRESHING!!")
        self.model.refresh()
        self.update_sidebar()


    def btn_add_run_clicked(self):
        print("Opening Add Run Dialog!")
        date, runTime, restTime, reps, note, result = AddRunDialog.AddRunDialog.getNewRunInfo()
        print( "date: " + date + "   runTime: " + str(runTime) + "   restTime: " + str(restTime) + "   reps: " + str(reps) + "   note: " + note + "   result: " + str(result))
        if result:
            self.model.addRun(date, runTime, restTime, reps, note)
            return


    def btn_settings_clicked(self, message=None):
        print("Opening Settings Dialog!")
        ip, database, table, user, password, result = SettingsDialog.SettingsDialog.getSettingsInfo(message)
        if result:
            self.model.setDatabaseInfo(ip, database, table, user, password)
            self.btn_refresh_clicked()


    def update_sidebar(self):
        self.summaryBrowser.setPlainText(
            "Total Run Count: " + str(self.model.rowCount()) + "\n"
        )


    def btn_sidebar_toggle(self):
        if self.sidebar_visible:
            self.summaryBrowser.hide()
            self.sidebar_visible = False
        else:
            self.summaryBrowser.show()
            self.sidebar_visible = True
        self.resizeEvent(None)

 
app = QtGui.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("res/ic_launcher.ico"))
myWindow = MyWindowClass(None)
# ui = Ui_MainWindow()
# ui.setupUi(myWindow)

myWindow.show()
app.exec_()

