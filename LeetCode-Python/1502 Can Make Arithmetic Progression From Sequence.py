"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

Example 1:
    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
    Input: arr = [1,2,4]
    Output: false
    Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:
    2 <= arr.length <= 1000
    -10^6 <= arr[i] <= 10^6
"""

def canMakeArithmeticProgression(arr):
    max_value = max(arr)
    min_value = min(arr)
    total_diff = max_value - min_value
    if total_diff == 0:
        return True
    nums_in_between = len(arr) - 2
    if total_diff % (nums_in_between + 1) != 0:
        return False
    else:
        nums = set(arr)
        for i in range(min_value, max_value + 1, total_diff // (nums_in_between + 1)):
            if i not in nums:
                return False
    return True
arr = [3,5,1]
print(canMakeArithmeticProgression(arr))

arr = [1,2,4]
print(canMakeArithmeticProgression(arr))

arr = [0,0,0,0]
print(canMakeArithmeticProgression(arr))
