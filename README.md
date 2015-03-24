RunLogDesktop
=============

This is a tool for viewing and adding runs to the RunLog database. It uses the PyQt4 and MySQLdb modules.

![RunLogDesktop GUI](https://raw.githubusercontent.com/davgra04/RunLogDesktop/master/screenshot5_mainwindow.png)


### Usage

To launch `RunLogDesktop`, simply run: 

`python RunLog.py`


### Requirements

**Python 2**

**PyQt4**

**MySQLdb**

Note: The tool has been tested on Windows with Python 2.7.9.


### Connecting

![RunLogDesktop GUI](https://raw.githubusercontent.com/davgra04/RunLogDesktop/master/screenshot6_onstart.png)

Upon launching `RunLogDesktop` (or by clicking "Settings") you are asked for the following connection information:

`Database IP` - IP address of the MySQL server hosting the RunLog.

`Database` - Name of the database to connect to.

`Table` - Name of the table to interact with.

`User` - User name for connecting to MySQL server.

`Password` - Password for connecting to MySQL server.


### Main UI

![RunLogDesktop GUI](https://raw.githubusercontent.com/davgra04/RunLogDesktop/master/screenshot5_mainwindow.png)

This is the main window of `RunLogDesktop`. The sidebar shows additional information about runs, and can be toggled. The following actions can be found in the toolbar:

`Refresh` - Refresh the contents of the table.

`Add Run` - Opens the Add Run dialog.

`Toggle Sidebar` - Shows/hides sidebar.

`Settings` - Opens the Settings dialog.


### Adding a Run

![RunLogDesktop GUI](https://raw.githubusercontent.com/davgra04/RunLogDesktop/master/screenshot4_addrundialog.png)

This is the dialog for adding a new run entry to the RunLog. The following options can be specified:

`Date` - The date of the run.

`Run Time` - Amount of time spent running each rep.

`Rest Time` - Amount of time spent resting each rep.

`Reps` - Number of reps.

`Note` - An optional note about the run.


### License

RunLogDesktop is distributed under The MIT License.


### Icons

UI Icons by Austin Andrews (@templarian) is licensed under CC BY-ND 3.0

