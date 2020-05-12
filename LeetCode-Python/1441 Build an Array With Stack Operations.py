"""
yue_xiao

LeetCode
5404. Build an Array With Stack Operations
User Accepted:2543
User Tried:2748
Total Accepted:2553
Total Submissions:3383
Difficulty:Easy
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.



Example 1:
    Input: target = [1,3], n = 3
    Output: ["Push","Push","Pop","Push"]
    Explanation:
    Read number 1 and automatically push in the array -> [1]
    Read number 2 and automatically push in the array then Pop it -> [1]
    Read number 3 and automatically push in the array -> [1,3]

Example 2:
    Input: target = [1,2,3], n = 3
    Output: ["Push","Push","Push"]

Example 3:
    Input: target = [1,2], n = 4
    Output: ["Push","Push"]
    Explanation: You only need to read the first 2 numbers and stop.

Example 4:
    Input: target = [2,3,4], n = 4
    Output: ["Push","Pop","Push","Push","Push"]

Constraints:
    1 <= target.length <= 100
    1 <= target[i] <= 100
    1 <= n <= 100
    target is strictly increasing.
"""


def buildArray(target, n):
    operations = list()
    index = 0
    for i in range(1, n + 1):
        if index == len(target):
            break
        if target[index] == i:
            operations.append('Push')
            index += 1
        else:
            operations.append('Push')
            operations.append('Pop')
    return operations

target1 = [1,3]
n1 = 3
print(buildArray(target1, n1))

target2 = [1, 2, 3]
n2 = 3
print(buildArray(target2, n2))

target3 = [1,2]
n3 = 4
print(buildArray(target3, n3))

target4 = [2,3,4]
n4 = 4
print(buildArray(target4, n4))
