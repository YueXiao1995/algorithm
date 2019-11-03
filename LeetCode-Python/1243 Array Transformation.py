"""
Given an initial array arr, every day you produce a new array using the array of the previous day.

On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:

If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.



Example 1:
    Input: arr = [6,2,3,4]
    Output: [6,3,3,4]
    Explanation:
    On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
    No more operations can be done to this array.

Example 2:
    Input: arr = [1,6,3,4,3,5]
    Output: [1,4,4,4,4,5]
    Explanation:
    On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
    On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
    No more operations can be done to this array.

Constraints:
    1 <= arr.length <= 100
    1 <= arr[i] <= 100
"""
def transformArray(arr):
    if len(arr) <= 2:
        return arr
    while True:
        is_changed = False
        new_arr = list()
        new_arr.append(arr[0])
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                new_arr.append(arr[i] + 1)
                is_changed = True
            elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                new_arr.append(arr[i] - 1)
                is_changed = True
            else:
                new_arr.append(arr[i])
        new_arr.append(arr[-1])
        arr = new_arr
        if not is_changed:
            break
    return arr

arr1 = [6,2,3,4]
arr2 = [1,6,3,4,3,5]
arr3 = [1, 2]
arr4 = [1]

print(transformArray(arr1))
print(transformArray(arr2))
print(transformArray(arr3))
print(transformArray(arr4))
