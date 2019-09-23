"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
    Input: [1,0,2,3,0,4,5,0]
    Output: null
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
    Input: [1,2,3]
    Output: null
    Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:
    1 <= arr.length <= 10000
    0 <= arr[i] <= 9
"""

def duplicateZeros(arr):
    i = 0
    l = len(arr)
    while i < l - 1: # because when 0 is in the last position, nothing will be changed, so here minus 1
        # if num equal to 0
        if arr[i] == 0:
            # move the remain to right
            # begin from the last num in list, each num equal to the num before it
            for j in reversed(range(i + 2, l)):
                arr[j] = arr[j - 1]
            # set the next num to 0
            arr[i + 1] = 0
            # skip those two 0
            i += 2
        else:
            i += 1
    return arr

input1 = [1,0,2,3,0,4,5,0]
input2 = [1,2,3]

print(duplicateZeros(input2))
