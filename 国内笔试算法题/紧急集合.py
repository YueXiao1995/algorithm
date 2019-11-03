

def minTimeNeeded(n, nums):
    max_distance = dict()
    i = 0
    while i < n:
        start = nums[i][:2]
        end = nums[i][2:4]
        v = nums[i][4]
        d = ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
        if v not in max_distance:
            max_distance[v] = d
        else:
            if max_distance[v] < d:
                max_distance[v] = d
        i += 1

    max_time = 0
    for v in max_distance.keys():
        t = (max_distance[v] ** 0.5) / v
        if t > max_time:
            max_time = t

    return keepThreeDigit(max_time)

def keepThreeDigit(num):
    num = float(num)
    num_string = str(num).split(".")
    if len(num_string[1]) > 3:
        num = num_string[0] + "." + num_string[1][:3]
    else:
        last_part = ("").join(["0"] * (3 - len(num_string[1])))

        num = num_string[0] + "." + num_string[1] + last_part
    return num

n = 2
nums = [[1, 1, 2, 2, 1],
        [1, 2, 2, 1, 1]]
print(minTimeNeeded(n, nums))

print(keepThreeDigit(1.4142135623730951))
