"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.


Example 1:
    Input: day = 31, month = 8, year = 2019
    Output: "Saturday"

Example 2:
    Input: day = 18, month = 7, year = 1999
    Output: "Sunday"

Example 3:
    Input: day = 15, month = 8, year = 1993
    Output: "Sunday"

Constraints:
    The given dates are valid dates between the years 1971 and 2100.
"""

def dayOfTheWeek(day, month, year):
    # the 1971, 1, 1 is Friday
    # for a given date, calculate the number of days between that day and 1997,1,1
    days = 0
    # first, add the total number of days between last year and 1997 to the days variable
    for i in range(1971, year):
        # if the year is the leap year, the year has 366 day
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            days += 366
        else:
            days += 365

    # the number of days in each month
    days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # add the number of days from january to last month
    for i in range(0, month - 1):
        days += days_by_month[i]

    # if it is a leap year and the target month later than february, plus one
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # in leap year february has 29 days
        if month > 2:
            days += 1

    # add the number of days in this month
    days += day

    # because 1971,1,1 already has one day, we need minus one
    days -= 1

    # because the 1971,1,1 is friday, so we can use the number of days between target date and that day,
    # to get the corresponding day of the week for that date.
    n = days % 7
    if n == 0:
        return "Friday"
    elif n == 1:
        return "Saturday"
    elif n == 2:
        return "Sunday"
    elif n == 3:
        return "Monday"
    elif n == 4:
        return "Tuesday"
    elif n == 5:
        return "Wednesday"
    elif n == 6:
        return "Thursday"


print(dayOfTheWeek(8, 9, 2019))
