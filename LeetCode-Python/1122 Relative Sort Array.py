"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


Example 1:
    Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    Output: [2,2,2,1,4,3,3,9,6,7,19]

Constraints:
    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    Each arr2[i] is distinct.
    Each arr2[i] is in arr1.
"""

def relativeSortArray(arr1, arr2):
    # iterate the arr2 to build a new list, so the order of nums is the same
    new_arr = list()
    l = len(arr1)
    for num in arr2:
        # iterate the arr1 to find the same num, add them into new list and delete them from arr1
        index = 0
        while index < l:
            if num == arr1[index]:
                # add to new arr
                new_arr.append(num)
                # remove from the arr1
                arr1.remove(num)
                l -= 1
            else:
                index += 1
    # sort the rest of the arr1 and append it to the new arr
    new_arr += sorted(arr1)
    return new_arr


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(relativeSortArray(arr1, arr2))
