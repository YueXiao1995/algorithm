"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

Example 1:
    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6

Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5
"""
def findSpecialInteger(arr):
    freq = dict()
    total_num = len(arr)
    lower_limit = total_num / 4
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    for num in freq:
        if freq[num] > lower_limit:
            return num

arr1 = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr1))
