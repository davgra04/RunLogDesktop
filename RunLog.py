from __future__ import print_function
from PyQt4 import QtGui, QtCore, uic
import sys, pprint
import icons_runlog_rc
import RunEntry, RunLogDao, RunTableModel

form_class = uic.loadUiType("ui_RunLog.ui")[0]                 # Load the UI

class MyWindowClass(QtGui.QMainWindow, form_class):

    console_table_printing_template = "{0:>5}  {1:>10}  {2:>11}  {3:>12}  {4:>4}  {5:103}"
    sidebar_visible = True

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # self.dao = RunLogDao.RunLogDao(testing=False)

        self.actionRefresh.triggered.connect(self.btn_refresh_clicked)
        self.actionToggle_Sidebar.triggered.connect(self.btn_sidebar_toggle)

        self.model = RunTableModel.RunTableModel()
        self.runTableView.setModel(self.model)

        self.btn_sidebar_toggle()   # Start with sidebar hidden
        self.btn_refresh_clicked()  # Start with a refresh

        self.resizeEvent(None)

    def resizeEvent(self, event):

        col_width = self.runTableView.width()/6

        self.runTableView.setColumnWidth(0, (col_width) if col_width < 30 else 30 )
        self.runTableView.setColumnWidth(1, (col_width) if col_width < 80 else 80 )
        self.runTableView.setColumnWidth(2, (col_width) if col_width < 80 else 80 )
        self.runTableView.setColumnWidth(3, (col_width) if col_width < 80 else 80 )
        self.runTableView.setColumnWidth(4, (col_width) if col_width < 60 else 60 )
        # self.runTableView.setColumnWidth(5, (col_width) if col_width < 30 else 30 )
        self.runTableView.horizontalHeader().setStretchLastSection(True)



# void QParent::resizeEvent(QResizeEvent *event) {
#     table_view->setColumnWidth(0, this->width()/3);
#     table_view->setColumnWidth(1, this->width()/3);
#     table_view->setColumnWidth(2, this->width()/3);

#     QMainWindow::resizeEvent(event);
# }

    def btn_refresh_clicked(self):
        print("REFRESHING!!")
        self.model.refresh()
        self.update_sidebar()

    def update_sidebar(self):
        self.summaryBrowser.setPlainText(
            "Total Run Count: " + str(self.model.rowCount()) + "\n" +
            "LULE\n" +
            "LULE\n" +
            "LULE\n" +
            "LULE\n"
        )

    def btn_sidebar_toggle(self):
        if self.sidebar_visible:
            self.summaryBrowser.hide()
            self.sidebar_visible = False
        else:
            self.summaryBrowser.show()
            self.sidebar_visible = True

 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()

