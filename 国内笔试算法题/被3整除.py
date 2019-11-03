"""
题目描述
    小Q得到一个神奇的数列: 1, 12, 123,...12345678910,1234567891011...。
    并且小Q对于能否被3整除这个性质很感兴趣。
    小Q现在希望你能帮他计算一下从数列的第l个到第r个(包含端点)有多少个数可以被3整除。
输入描述:
    输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。
输出描述:
    输出一个整数, 表示区间内能被3整除的数字个数。

示例1
    输入
        2 5
    输出
        3

    说明
        12, 123, 1234, 12345...
        其中12, 123, 12345能被3整除。
"""

import sys

l = 0
r = 0
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        l = int(lines[0])
        r = int(lines[1])
except:
    pass

def getThePreviousNumber(index):
    num = ""
    for i in range(1, index):
        num += str(i)
    return num

def function(l, r):
    result = 0
    num = getThePreviousNumber(l)
    for i in range(l, r + 1):
        num = num + str(i)
        if int(num) % 3 == 0:
            result += 1
    return result

def function2(l, r):
    result = 0
    previous_sum_of_digits = 0
    i = 1
    while i < l:
        previous_sum_of_digits += i
        if previous_sum_of_digits % 3 == 0:
            previous_sum_of_digits = 0
        i += 1

    i = l
    while i < r + 1:
        previous_sum_of_digits += i
        if previous_sum_of_digits % 3 == 0:
            result += 1
            previous_sum_of_digits = 0
        i += 1
    return result

def function3(l, r):
    result = 0
    i = l
    while i < r + 1:
        if i % 3 != 1:
            result += 1
        i += 1
    return result

def function4(l, r):
    result = 0

    while l % 3 != 1:
        result += 1
        l += 1

    while r % 3 != 0:
        if r % 3 != 1:
            result += 1
        r -= 1

    result += ((r - l + 2) // 3) * 2
    return result


print(function2(l, r))
print(function3(l, r))
print(function4(l, r))

