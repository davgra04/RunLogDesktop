from __future__ import print_function
import MySQLdb as mdb
import sys, pprint
import RunEntry, RunLogDao

console_table_printing_template = "{0:>5}  {1:>10}  {2:>11}  {3:>12}  {4:>4}  {5:103}"

dao = RunLogDao.RunLogDao(testing=True)

columns = dao.getColumns()
my_runs = dao.getRuns()

print( console_table_printing_template.format(columns[0], columns[1], columns[2], columns[3], columns[4], columns[5]) )

for run in my_runs:
    # pprint.pprint(run)
    print( run.get_details_string(truncate=True) )