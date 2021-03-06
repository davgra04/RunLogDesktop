from __future__ import print_function
import sys, pprint

# Object for accessing the runlog database
class RunEntry:

    console_table_printing_template = "{0:>5}  {1:>10}  {2:>11}  {3:>12}  {4:>4}  {5:103}"
    truncate_length = 60


    def __init__(self, input_date, input_seconds_run, input_seconds_rest, input_reps, input_run_id=-1):
        self.run_id = input_run_id
        self.date = input_date
        self.seconds_run = input_seconds_run
        self.seconds_rest = input_seconds_rest
        self.reps = input_reps
        return


    def __init__(self, input_date, input_seconds_run, input_seconds_rest, input_reps, input_note, input_run_id=-1):
        self.run_id = input_run_id
        self.date = input_date
        self.seconds_run = input_seconds_run
        self.seconds_rest = input_seconds_rest
        self.reps = input_reps
        self.note = input_note
        return


    def get_details_string(self, truncate=False):
        printed_note = self.note
        if printed_note is None:
            printed_note = "--"
        if truncate:
            printed_note = (printed_note[:self.truncate_length] + '...') if len(printed_note) > self.truncate_length else printed_note

        return self.console_table_printing_template.format(self.run_id, self.date.strftime('%Y/%m/%d'), self.seconds_run, self.seconds_rest, self.reps, printed_note)


    ### Getters
    def get_id(self):
        return self.run_id

    def get_date(self):
        return self.date

    def get_date_string(self):
        return self.date.strftime('%Y/%m/%d')

    def get_sec_run(self):
        return self.seconds_run

    def get_sec_rest(self):
        return self.seconds_rest

    def get_reps(self):
        return self.reps

    def get_note(self):
        return self.note

