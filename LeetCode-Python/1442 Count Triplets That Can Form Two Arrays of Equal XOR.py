"""
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

Example 1:
    Input: arr = [2,3,1,6,7]
    Output: 4
    Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
    Input: arr = [1,1,1,1,1]
    Output: 10

Example 3:
    Input: arr = [2,3]
    Output: 0

Example 4:
    Input: arr = [1,3,5,7,9]
    Output: 3

Example 5:
    Input: arr = [7,11,12,9,5,2,7,17,22]
    Output: 8

Constraints:
    1 <= arr.length <= 300
    1 <= arr[i] <= 10^8
"""
# Time Limit Execed
"""
def countTriplets(arr):
    def orx(arr, a, b):
        result = arr[a]
        for i in range(a + 1, b):
            result ^= arr[i]
        return result

    tuples = set()
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            a = orx(arr, i, j)
            for k in range(j, len(arr)):
                b = orx(arr, j, k + 1)
                if a == b:
                    tuples.add((i, j, k))
    return len(tuples)
"""

# if a == b, then a ^ b == 0
def countTriplets(arr):
    n = 0
    for i in range(len(arr) - 1):
        a = arr[i]
        # here we dont need to consider the j,
        # because what we what is a = b, which means                     a                   ^                      b               = 0,
        #                                           (arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]) ^ (arr[j] ^ arr[j + 1] ^ ... ^ arr[k]) = 0
        for k in range(i + 1, len(arr)):
            a ^= arr[k]
            if a == 0:
                n += k - i
    return n

arr1 = [2,3,1,6,7]
print(countTriplets(arr1))

arr2 = [1,1,1,1,1]
print(countTriplets(arr2))

arr3 = [2,3]
print(countTriplets(arr3))

arr4 = [1,3,5,7,9]
print(countTriplets(arr4))

arr5 = [7,11,12,9,5,2,7,17,22]
print(countTriplets(arr5))

print(1^4)
