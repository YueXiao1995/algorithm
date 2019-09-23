"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:
    Input: [4,2,5,7]
    Output: [4,5,2,7]
    Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Note:
    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000
"""

def sortArrayByParityII(A):
    # store the odd and even nums into two list
    odd_list = list()
    even_list = list()
    # iterate the list A to find all of the odd and even numbers
    for num in A:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    # use the odd list and even list to generate a new list
    new_list = list()
    for i in range(0, len(odd_list)):
        new_list.append(even_list[i])
        new_list.append(odd_list[i])
    return new_list


input1 = [4,2,5,7]
print(sortArrayByParityII(input1))
