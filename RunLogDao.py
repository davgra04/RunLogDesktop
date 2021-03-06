from __future__ import print_function
import MySQLdb as mdb
import sys, pprint
from datetime import date
import RunEntry

# Object for accessing the runlog database
class RunLogDao:

    def __init__(self, testing=False):

        self.db_testing = testing
        return


    def setConnectionInfo(self, ip, database, table, user, password):

        self.db_ip = ip
        self.db_database = database
        self.db_table = table
        self.db_user = user
        self.db_pw = password

        return


    def getColumns(self):

        if self.db_testing:
            return ["id", "date", "seconds_run", "seconds_rest", "reps", "note"]

        cols = []

        if self._connect():

            if self.con:
                cur = self.con.cursor()
                cur.execute("SELECT * FROM " + self.db_table )
                desc = cur.description
                for col in desc:
                    cols.append(col[0])

            self._disconnect()

        return cols


    def get_test_runs(self):

        runs = []
        for index in range(0,20):
            runs.append( RunEntry.RunEntry(date(2015, 3, 22), 70, 230, 1337, "HUE HUE HUE", input_run_id=1337+index) )
        return runs


    def getRuns(self):

        if self.db_testing:
            return self.get_test_runs()

        runs = []

        if self._connect():

            if self.con:
                cur = self.con.cursor()
                cur.execute("SELECT * FROM " + self.db_table + " ORDER BY `date` DESC")
                rows = cur.fetchall()
                for row in rows:
                    runs.append( RunEntry.RunEntry(row[1], row[2], row[3], row[4], row[5], input_run_id=row[0]) )

            self._disconnect()

        return runs


    def addRun(self, date, runTime, restTime, reps, note):
        # print("RunLogDao:Adding Run!")
        if self.db_testing:
            print("Pretending to add run:")
            print( "    date: " + date + "   runTime: " + str(runTime) + "   restTime: " + str(restTime) + "   reps: " + str(reps) + "   note: " + note + "   result: " + str(result))
            return

        if self._connect():

            if self.con:
                cur = self.con.cursor()

                if note:
                    cur.execute("INSERT INTO `" + self.db_table + "` (`date`, `seconds_run`, `seconds_rest`, `reps`, `notes`) VALUES (%s, %s, %s, %s, %s)", (date, runTime, restTime, reps, note))
                else:
                    cur.execute("INSERT INTO `" + self.db_table + "` (`date`, `seconds_run`, `seconds_rest`, `reps`) VALUES (%s, %s, %s, %s)", (date, runTime, restTime, reps))

                cur.close()
                self.con.commit()
                print("Number of rows inserted: " + str(cur.rowcount))

            self._disconnect()


    # Opens connection to DB
    def _connect(self):
        try:
            self.con = mdb.connect(self.db_ip, self.db_user, self.db_pw, self.db_database)
            return True
        except mdb.Error, e:
            print( "Error %d: %s" % (e.args[0],e.args[1]) )
            return False


    # Closes connection to DB
    def _disconnect(self):
        if self.con:
            self.con.close()
        return

