"""

"""
import sys

#for line in sys.stdin:
#    a = line.split()
#    print(int(a[0]) + int(a[1]))
"""
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

def convert(s):
    if_valid = False
    invalid = ['], ', ', [', '][']

    substring = ""
    start = 0
    for i in range(len(s)):
        if s[i].isdigit() == False:
            if substring == "":
                start = i
            substring += s[i]
        else:
            if substring in invalid:
                s = s[0: start] + '], [' + s[i:]
            substring = ''

    nodes = s.split("], [")
    print(nodes)

    print(s)

    return 0
"""
input_value = list()
for line in sys.stdin:
    input_value = line
    break
print(input_value)
"""
input1 = "[[5, 2, 5], [6, 5, 6, [4, 1, 4], [2, 4, 2], [1, 0, 1]]"

print(convert(input1))
