"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
    Input: date1 = "2019-06-29", date2 = "2019-06-30"
    Output: 1

Example 2:
    Input: date1 = "2020-01-15", date2 = "2019-12-31"
    Output: 15

Constraints:
    The given dates are valid dates between the years 1971 and 2100.
"""

def daysBetweenDates(date1, date2):
    day_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date1 = [int(date1[:4]), int(date1[5:7]), int(date1[8:])]
    date2 = [int(date2[:4]), int(date2[5:7]), int(date2[8:])]

    earlier_year = min(date1[0], date2[0])

    def isLeapYear(y):
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    return True
            else:
                return True
        return False

    def daysFromANewYearToADate(earlier_year, date):
        days = 0
        for y in range(earlier_year, date[0] + 1):
            is_leap_year = isLeapYear(y)

            if y == date[0]:
                for m in range(date[1]):
                    if m == date[1] - 1:
                        days += date[2]
                    else:
                        days += day_in_months[m]
                        if m == 1 and is_leap_year:
                            days += 1
            else:
                if is_leap_year:
                    days += 366
                else:
                    days += 365
        return days

    d1 = daysFromANewYearToADate(earlier_year, date1)
    d2 = daysFromANewYearToADate(earlier_year, date2)

    return abs(d2-d1)

date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1, date2))

date1 = "2020-01-15"
date2 = "2019-12-31"
print(daysBetweenDates(date1, date2))


date1 = "2074-09-12"

date2 = "1983-01-08"
print(daysBetweenDates(date1, date2))
