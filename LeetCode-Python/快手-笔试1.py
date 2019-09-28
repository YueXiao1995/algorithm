"""
输入输出示范：

import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

输入输出示范：

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
"""
def isAbleToAttend(n, timetable):
    # a list to record the earliest end and latest start time for each event
    time_rule = list()
    for event in timetable:
        min_time_needed = (event[1]-event[0]) // 2 + 1
        latest_start = event[1] - min_time_needed
        earliest_end = event[0] + min_time_needed
        time_rule.append([latest_start, earliest_end])
    time_rule = sorted(time_rule)
    for i in range(1, n):
        print(i)
        if time_rule[i-1][1] > time_rule[i][0]:
            print(i)
            print(time_rule[i-1][1])
            return -1
    return 1

n1 = 4
timetable1 = [[3, 10], [1, 5], [4, 6], [3, 5]]

print(isAbleToAttend(n1, timetable1))

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = list()
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        s = str(line).split(" ")
        for i in range(len(s)):
            s[i] = int(s[i])
        ans.append(s)
    print(n)
    print(ans)
    print(isAbleToAttend(n, ans))
