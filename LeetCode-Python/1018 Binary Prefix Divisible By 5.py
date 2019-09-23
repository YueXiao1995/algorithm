"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:
    Input: [0,1,1]
    Output: [true,false,false]
    Explanation:
    The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

Example 2:
    Input: [1,1,1]
    Output: [false,false,false]

Example 3:
    Input: [0,1,1,1,1,1]
    Output: [true,false,false,false,true,false]

Example 4:
    Input: [1,1,1,0,1]
    Output: [false,false,false,false,false]
"""


# Time Limit Exceeded
"""
def prefixesDivBy5(A):
    nums = list()

    for i in range(len(A)):
        subarray = list(A)[:i + 1]
        nums.append(subarray)
    print(nums)

    result = list()

    base_10_num = list()
    for num in nums:
        base_10 = 0
        time = 1
        for i in reversed(range(len(num))):
            base_10 += num[i] * time
            time *= 2
        if base_10 % 5 == 0:
            result.append(True)
        else:
            result.append(False)
        base_10_num.append(base_10)
    print(base_10_num)

    return result

"""

def prefixesDivBy5(A):
    result = list()
    l = len(A)
    last_base_10 = 0
    for i in range(l):
        last_base_10 = last_base_10 * 2 + A[i]
        if last_base_10 % 5 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

input = [0,1,1]
input2 = [1,1,1]
input3 = [0,1,1,1,1,1]
input4 = [1,1,1,0,1]


print(prefixesDivBy5(input4))
