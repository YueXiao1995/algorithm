"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:
    Input: [1,2,2,3]
    Output: true

Example 2:
    Input: [6,5,4,4]
    Output: true

Example 3:
    Input: [1,3,2]
    Output: false

Example 4:
    Input: [1,2,4,5]
    Output: true

Example 5:
    Input: [1,1,1]
    Output: true

Note:
    1 <= A.length <= 50000
    -100000 <= A[i] <= 100000
"""

def isMonotonic(A):
    # a variable used to record last num
    last = None

    is_increasing = None
    # iterate the list
    for num in A:
        # if the num is not the first element in list
        if last != None:
            # if the last num is smaller than this num
            if last < num:
                # if this is the first unequal num, temporarily think this array is monotone increasing
                if is_increasing == None:
                    is_increasing = True
                # else if previously think the array is monotone decreasing, but now violated, return False
                elif is_increasing == False:
                    return False
            # if the last num is bigger than this num
            elif last > num:
                # if this is the first unequal num, temporarily think this array is monotone decreasing
                if is_increasing == None:
                    is_increasing = False
                # else if previously think the array is monotone decreasing, but now violated， return False
                elif is_increasing == True:
                    return False
        # update the last num
        last = num
    return True

input1 = [1, 2, 2, 3]
input2 = [6,5,4,4]
input3 = [1,3,2]
input4 = [1,2,4,5]
input5 = [1,1,1]

print(isMonotonic(input3))
