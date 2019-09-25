"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:
    Input: [1,2,3,4]
    Output: "23:41"

Example 2:
    Input: [5,5,5,5]
    Output: ""

Note:
    A.length == 4
    0 <= A[i] <= 9
"""

def largestTimeFromDigits(A):
    max_hour = 0
    max_time = dict()
    for i in range(4):
        for j in range(i + 1, 4):
            hour_1 = int(str(A[i])+str(A[j]))
            hour_2 = int(str(A[j])+str(A[i]))
            if hour_1 < 24:
                if hour_1 >= max_hour:
                    copy_A = A.copy()
                    del copy_A[j]
                    del copy_A[i]
                    minute_1 = int(str(copy_A[0]) + str(copy_A[1]))
                    minute_2 = int(str(copy_A[1]) + str(copy_A[0]))

                    if min(minute_1, minute_2) < 60 and  hour_1 >= max_hour:
                        max_hour = hour_1
                        if minute_1 < 60:
                            if hour_1 not in max_time:
                                max_time = {hour_1: minute_1}
                            else:
                                if minute_1 > max_time[hour_1]:
                                    max_time[hour_1] = minute_1
                        if minute_2 < 60:
                            if hour_1 not in max_time:
                                max_time = {hour_1: minute_2}
                            else:
                                if minute_2 > max_time[hour_1]:
                                    max_time[hour_1] = minute_2
            if hour_2 < 24:
                if hour_2 >= max_hour:
                    copy_A = A.copy()
                    del copy_A[j]
                    del copy_A[i]
                    minute_1 = int(str(copy_A[0]) + str(copy_A[1]))
                    minute_2 = int(str(copy_A[1]) + str(copy_A[0]))
                    if min(minute_1, minute_2) < 60 and hour_2 >= max_hour:
                        max_hour = hour_2
                        if minute_1 < 60:
                            if hour_2 not in max_time:
                                max_time = {hour_2: minute_1}
                            else:
                                if minute_1 > max_time[hour_2]:
                                    max_time[hour_2] = minute_1
                        if minute_2 < 60:
                            if hour_2 not in max_time:
                                max_time = {hour_2: minute_2}
                            else:
                                if minute_2 > max_time[hour_2]:
                                    max_time[hour_2] = minute_2

    # if the max_time dict is empty, return ""
    if len(max_time) == 0:
        return ""
    # else form a string by using the max_time
    else:
        minute = max_time[max_hour]
        # if the num smaller than 10, add a "0" in front of the num
        if max_hour < 10:
            hour = "0" + str(max_hour)
        else:
            hour = str(max_hour)

        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)

        return hour + ":" + minute

input1 = [1,2,3,4]
input2 = [5,5,5,5]
input3 = [0, 0, 0, 0]
input4 = [0, 0, 2, 3]
input5 = [0, 0, 3, 0]

print(largestTimeFromDigits(input5))
