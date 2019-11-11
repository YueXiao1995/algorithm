"""
https://leetcode.com/problems/pancake-sorting/
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:
    Input: [3,2,4,1]
    Output: [4,2,4,3]
    Explanation:
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.

Example 2:
    Input: [1,2,3]
    Output: []
    Explanation: The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.

Note:
    1 <= A.length <= 100
    A[i] is a permutation of [1, 2, ..., A.length]
"""

def pancakeSort(A):
    output = list()
    l = len(A)
    index = l - 1
    # sort the num from the largest to the smallest
    while index > 0:
        # find the index of the maximum value
        max_index = index
        max_value = A[index]
        for i in range(index):
            if A[i] > max_value:
                max_index = i
                max_value = A[i]
        # if the max value is not the last one
        if max_index != index:
            # if the max value is not the first one
            if max_index != 0:
                # the part should be flip to move the maximum to the start of the list
                flip_part = A[:max_index + 1]
                # flip the part
                flip_part.reverse()
                # form the new A
                A = flip_part + A[max_index + 1:]
                # add the length of this flip part to the output list
                output.append(max_index + 1)
            # reverse the A, move the max value to the end of the l;ist
            A.reverse()
            # append the length of A to the output list
            output.append(index + 1)
            # remove the max value which is now in the end of the list A
            A.pop(-1)
        else:
            # remove the max value
            A.pop(-1)
        index -= 1
    return output

input1 = [3, 2, 4, 1]
input2 = [1, 2, 3]
input3 = [1, 4, 2, 3]

print(pancakeSort(input1))
print(pancakeSort(input2))
print(pancakeSort(input3))
