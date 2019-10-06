"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:
    Input:
    Output: [1,5]
    Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:
    1 <= arr1.length, arr2.length, arr3.length <= 1000
    1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""

def arraysIntersection(arr1, arr2, arr3):
    set_1 = set(arr1)
    set_2 = set(arr2)
    set_3 = set(arr3)
    common_num = set_1 & set_2 & set_3
    return sorted(list(common_num))


arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

print(arraysIntersection(arr1, arr2, arr3))
