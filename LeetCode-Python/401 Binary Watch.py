"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:
    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
def readBinaryWatch(num):
    # the number of each LED
    first_row = [8, 4, 2, 1]
    second_row = [32, 16, 8, 4, 2, 1]
    # generate all of the possible sequence of hour
    possible_hours = [[[0, 0, 0, 0]]]
    # the maximum number of LEDs that are currently on in hour row is 3
    for i in range(3):
        new_possible_hours = list()
        for hours in possible_hours[i]:
            for k in range(4):
                if hours[k] == 0:
                    copy = list(hours)
                    copy[k] = first_row[k]
                    new_possible_hours.append(copy)
        possible_hours.append(new_possible_hours)
    # convert the binary number to int, omit the number bigger than 11
    valid_hours = list()
    for hours_list in possible_hours:
        hours_set = set()
        for hours in hours_list:
            if sum(hours) < 12:
                hours_set.add(sum(hours))
        valid_hours.append(list(hours_set))

    # generate all of the possible sequence of minute
    possible_minute = [[[0, 0, 0, 0, 0, 0]]]
    for i in range(5):
        new_possible_minute = list()
        for minute in possible_minute[i]:
            for k in range(6):
                if minute[k] == 0:
                    copy = list(minute)
                    copy[k] = second_row[k]
                    new_possible_minute.append(copy)
        possible_minute.append(new_possible_minute)

    valid_minute = list()
    for minute_list in possible_minute:
        minute_set = set()
        for minute in minute_list:
            if sum(minute) < 60:
                minute_set.add(sum(minute))
        valid_minute.append(list(minute_set))

    result = list()
    # the num of LEDs that are currently on in the first row
    i = 0
    # break the loop when the num of LEDs in the first row beyond the limitation
    # or there is no more LEDs left
    while i < 4 and num >= 0:
        if num < 6:
            hours = valid_hours[i]
            minutes = valid_minute[num]
            for hour in hours:
                for minute in minutes:
                    if minute < 10:
                        minute = "0" + str(minute)
                    result.append(str(hour) + ":" + str(minute))
        i += 1
        num -= 1
    return result

input1 = 6
print(readBinaryWatch(input1))
