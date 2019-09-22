"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]

Example 3:
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]

Constraints:
    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6
"""

# Time Limit Exceeded
"""
def minimumAbsDifference(arr):
    arr = sorted(arr)
    min_diff = None
    pairs = list()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = arr[j] - arr[i]
            if min_diff == None:
                min_diff = diff
                pairs.append([arr[i], arr[j]])
            else:
                if diff < min_diff:
                    min_diff = diff
                    pairs = [[arr[i], arr[j]]]
                elif diff == min_diff:
                    pairs.append([arr[i], arr[j]])
            print(diff)
    return pairs
"""
def minimumAbsDifference(arr):
    # sort the arr
    arr = sorted(arr)
    min_diff = None
    # use a list to record the pairs with minimum difference
    pairs = list()
    # use a variable to record the last num in arr
    last = arr[0]
    # iterate over the arr, to find the adjacent nums which has the min diff
    for i in range(1, len(arr)):
        diff = arr[i] - last        # calculate the difference
        if min_diff == None:        # if min diff is None, initial it
            min_diff = diff
            pairs.append([last, arr[i]]) # append this pair to the pairs list
        else:
            if diff < min_diff:             # if the diff is smaller then the min diff,
                min_diff = diff             # up date the min diff
                pairs = [[last, arr[i]]]    # up date the min diff and reset the pairs list
            elif diff == min_diff:          # if the diff is equal to min diff
                pairs.append([last, arr[i]])# append the pair to the pairs list
        last = arr[i]   # update the last
    return pairs
arr1 = [4,2,1,3]
arr2 = [1,3,6,10,15]
arr3 = [3,8,-10,23,19,-4,-14,27]
arr4 = [40,11,26,27,-20]
print(minimumAbsDifference(arr4))
