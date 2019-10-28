"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
    Input: target = 3
    Output: 2
    Explanation:
    On the first move we step from 0 to 1.
    On the second step we step from 1 to 3.

Example 2:
    Input: target = 2
    Output: 3
    Explanation:
    On the first move we step from 0 to 1.
    On the second move we step  from 1 to -1.
    On the third move we step from -1 to 2.

Note:
    target will be a non-zero integer in the range [-10^9, 10^9].
"""
"""
def reachNumber(target):
    target = abs(target)
    if target >= 0:
        step_size = 1
        position = 0
        while position + step_size < target:
            position += step_size
            step_size += 1
        print(position)
        print(step_size)
        if position + step_size == target:
            return step_size
        else:
            step_size -= 1
            step_size += (target - position) * 2
            return step_size
    else:
        step_size = 1
        position = 0
        while position - step_size > target:
            position -= step_size
            step_size += 1
        print(position)
        print(step_size)
        if position - step_size == target:
            return step_size
        else:
            step_size -= 1
            step_size += (position - target) * 2
            return step_size
"""
def reachNumber(target):
    target = abs(target)
    if target == 0:
        return 0
    step = 0
    step_size = 1
    position = 0
    while position < target:
        position += step_size
        step_size += 1
        step += 1
        if position == target:
            return step
    step -= 1
    step_size -= 1
    position -= step_size
    diff = target - position
    return step + diff * 2


target1 = 3
target2 = 2
target3 = 4
target4 = -2
target5 = 0

print(reachNumber(target1))
print(reachNumber(target2))
print(reachNumber(target3))
print(reachNumber(target4))
print(reachNumber(target5))

