"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:
    Input: [0,2,1,-6,6,-7,9,1,2,0,1]
    Output: true
    Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
    Input: [0,2,1,-6,6,7,9,-1,2,0,1]
    Output: false

Example 3:
    Input: [3,3,6,5,-2,2,5,1,-9,4]
    Output: true
    Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Note:
    3 <= A.length <= 50000
    -10000 <= A[i] <= 10000
"""

def canThreePartsEqualSum(A):
    # calculate the sum of the list A
    sum = 0
    for num in A:
        sum += num
    # if the sum can not exact division 3, then return False
    if sum % 3 != 0:
        return False
    else:
        sum = int(sum / 3)
    # check if these three parts exist
    temp_sum = 0
    num_of_part = 0
    for num in A:
        temp_sum += num
        # if the temp sum equal target sum, reset the temp sum to 0, and number of part plus 1
        if temp_sum == sum:
            temp_sum = 0
            num_of_part += 1
    # check if there are 3 equal parts and if the last element is the end of third parts
    if temp_sum != 0 or num_of_part != 3:
        return False
    else:
        return True

input1 = [0,2,1,-6,6,-7,9,1,2,0,1]
input2 = [0,2,1,-6,6,7,9,-1,2,0,1]
input3 = [3,3,6,5,-2,2,5,1,-9,4]

print(canThreePartsEqualSum(input1))
