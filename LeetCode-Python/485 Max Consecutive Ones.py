"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.

Note:
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""
def findMaxConsecutiveOnes(nums):
    max_l = 0
    temp_l = 0
    for num in nums:
        # if num is 1, increase the temp_l by one, and update the max_l
        if num == 1:
            temp_l += 1
            if temp_l > max_l:
                max_l = temp_l
        else:
            temp_l = 0
    return max_l


# test cases
input = [1,1,0,1,1,1]
input2 = [0]
input3 = [1]

# test
print(findMaxConsecutiveOnes(input3))
