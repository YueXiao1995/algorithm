"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.


Example 1:
    Input: [3,2,3]
    Output: 3

Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2
"""
def majorityElement(nums):
    freq = dict()
    for num in nums:
        if num not in freq:
            freq[num] = 0
        else:
            freq[num] += 1
    return max(freq, key=freq.get)


input1 = [3,2,3]
input2 = [2,2,1,1,1,2,2]

print(majorityElement(input1))
