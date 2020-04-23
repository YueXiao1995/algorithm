"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:
    Input: arr = [10,2,5,3]
    Output: true
    Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
    Input: arr = [7,1,14,11]
    Output: true
    Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
    Input: arr = [3,1,7,11]
    Output: false
    Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:
    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
"""

def checkIfExist(arr):
    num_set = set(arr)
    l = len(arr)
    i = 0
    while i < l:
        if arr[i] == 0:
            del arr[i]
            l -= 1
            if 0 in arr:
                return True
        else:
            if 2 * arr[i] in num_set:
                return True
            i += 1
    return False

arr1 = [10,2,5,3]
arr2 = [7,1,14,11]
arr3 = [3,1,7,11]
arr4 = [0, 0]
arr5 = [-2,0,10,-19,4,6,-8]
print(checkIfExist(arr5))

