from __future__ import print_function
import MySQLdb as mdb
import sys, pprint

console_table_printing_template = "{0:3}  {1:10}  {2:11}  {3:12}  {4:4}  {5:103}"
truncate_length = 60

def print_run_table_to_console(connection):

    cur = connection.cursor()
    cur.execute("SELECT * FROM runlog")
    rows = cur.fetchall()

    desc = cur.description
    # pprint.pprint(desc)

    print(console_table_printing_template.format(desc[0][0], desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0]))

    for row in rows:
        # print(row)
        
        note = None
        if row[5] is not None:
            note = (row[5][:truncate_length] + '...') if len(row[5]) > truncate_length else row[5]

        print(console_table_printing_template.format(row[0], row[1].strftime('%Y/%m/%d'), row[2], row[3], row[4], note))

    return

try:
    con = mdb.connect('10.0.0.218', 'dbADMEEN', 'joshIsAHagmo', 'personalDB');

    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print( "Database version : %s " % ver )

    print_run_table_to_console(con)

    
except mdb.Error, e:
  
    print( "Error %d: %s" % (e.args[0],e.args[1]) )
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()