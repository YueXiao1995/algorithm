"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
    1 <= A.length <= 5000
    0 <= A[i] <= 5000
"""


def sortArrayByParity(A):
    # store the odd and even nums into two list
    odd_list = list()
    even_list = list()
    # iterate the list A to find all of the odd and even numbers
    for num in A:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list + odd_list




input  = [3,1,2,4]
print(sortArrayByParity(input))
