"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
  - If the user doesn't specify any input, your program should
    print the calendar for the current month. The 'datetime'
    module may be helpful for this.
  - If the user specifies one argument, assume they passed in a
    month and render the calendar for that month of the current year.
  - If the user specifies two arguments, assume they passed in
    both the month and the year. Render the calendar for that
    month and year.
  - Otherwise, print a usage statement to the terminal indicating
    the format that your program expects arguments to be given.
    Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


# ? to grab current year and month for default values
current_date = datetime.now()
month = current_date.month
year = current_date.year

# ? to change values of global variables when sys.argv[1] is provided
def change_month(new_month):
    global month
    month = new_month


# ? to change values of global variables when sys.argv[2] is provided
def change_year(new_year):
    global year
    year = new_year


# ? if else statement to check if any command line args were provided
if (len(sys.argv) == 2):
    change_month(int(sys.argv[1]))
    # ? If the user specifies one arguments, assume they passed in the month, update month by calling change_month() and leave year as default of current_date.year

elif(len(sys.argv) == 3):
    change_month(int(sys.argv[1]))
    change_year(int(sys.argv[2]))
    # ? If the user specifies two arguments, assume they passed in both the month and the year, update both month and year from defaults by calling change_month() and change_year()

# ? print call
print(calendar.month(year, month))