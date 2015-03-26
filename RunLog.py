from __future__ import print_function
from PyQt4 import QtGui, QtCore, uic
from ui_RunLog import Ui_MainWindow
import sys, pprint
import icons_runlog_rc
import RunEntry, RunLogDao, RunTableModel, SettingsDialog, AddRunDialog

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

        # Connect toolbar actions to handlers
        self.actionRefresh.triggered.connect(self.btn_refresh_clicked)
        self.actionToggle_Sidebar.triggered.connect(self.btn_sidebar_toggle)
        self.actionSettings.triggered.connect(self.btn_settings_clicked)
        self.actionAddRun.triggered.connect(self.btn_add_run_clicked)

        # Set up table model
        self.model = RunTableModel.RunTableModel()
        self.runTableView.setModel(self.model)
        self.columnMinSizes = [40, 80, 80, 80, 40, 100]

        QtCore.QTimer.singleShot(100, self.OnLoad)


    def OnLoad(self):
        # Launch settings dialog for database connection/settings
        self.btn_settings_clicked(message="Input database connection info to connect.")
        # self.btn_refresh_clicked()
        self.resizeEvent(None)


    def resizeEvent(self, event):

        col_width = self.runTableView.width() / (len(self.columnMinSizes)+3)
        for index in range(self.model.columnCount()):
            self.runTableView.setColumnWidth(index, (col_width) if col_width < self.columnMinSizes[index] else self.columnMinSizes[index])

        self.runTableView.horizontalHeader().setStretchLastSection(True)


    def btn_refresh_clicked(self):
        # print("REFRESHING!!")
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
app.setWindowIcon(QtGui.QIcon("ic_launcher.ico"))
myWindow = MyWindowClass(None)

myWindow.show()
app.exec_()

