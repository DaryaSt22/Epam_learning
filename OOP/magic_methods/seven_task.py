# Create a context manager LogFile inherited from ContextDecorator which adds text lines into a log file. Every text line must contain the following information:
#
# date and time when started (Start:)
# execution time (Run:)
# error information (in the code wrapped by context manager) (An error occured:)
# The trace format example when no errors occurred:
#
# Start: 2021-03-22 12:38:24.757637 | Run: 0:00:00.000054 | An error occurred: None
# The example in case of ZeroDivisionError exception
#
# Start: 2021-03-22 12:38:24.758463 | Run: 0:00:00.000024 | An error occurred: division by zero
# The log file name is passed as an argument to text manager constructor. For example:
#
# @LogFile('my_trace.log')
# def some_func():
#     ...
# The log file has to be open in append mode to allow reopening existing file and adding new information into this file if the same name is pointed.
#
# When an exception is happened the error message has to be put in An error occured: into the log and reraised upper.
#
# Use open builtin function to open the log file.


from datetime import datetime
from contextlib import ContextDecorator


class LogFile(ContextDecorator):

    def __init__(self, filename):
        self._filename = filename

    def __enter__(self):
        start_time = datetime.now()
        self._start_time = start_time

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.now()
        self.run = self.end_time - self._start_time
        if exc_val is None:
            error_text = None
        else:
            error_text = str(exc_val)
        line = f"Start: {self._start_time} | Run: {self.run} | An error occurred: {error_text}"
        with open(self._filename, 'a', encoding='utf-8') as file:
            file.write(line + "\n")
