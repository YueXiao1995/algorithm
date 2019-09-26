"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.



Example 1:
    Input: date = "2019-01-09"
    Output: 9
    Explanation: Given date is the 9th day of the year in 2019.

Example 2:
    Input: date = "2019-02-10"
    Output: 41

Example 3:
    Input: date = "2003-03-01"
    Output: 60

Example 4:
    Input: date = "2004-03-01"
    Output: 61

Constraints:
    date.length == 10
    date[4] == date[7] == '-', and all other date[i]'s are digits
    date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""

def dayOfYear(date):
    # the num of days in each month in a year which is not a leap year
    num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # split the date string
    date = date.split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    # check if the year is a leap year
    is_leap_year = False
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        is_leap_year = True
    # add the sum of the days in previous months
    day_of_year = 0
    for i in range(0, month - 1):
        day_of_year += num_of_days[i]
        # if month bigger than 2 and it is a leap year, add one more day
        if i == 1:
            if is_leap_year:
                day_of_year += 1
    # add the days in that month
    day_of_year += day
    return day_of_year


date1 = "2019-01-09"
date2 = "2019-02-10"
date3 = "2003-03-01"
date4 = "2004-03-01"
date5 = "1900-03-25"

print(dayOfYear(date5))
