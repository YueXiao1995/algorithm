"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.



Example 1:
    Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
    Output: [8,6,2,4]

    Explanation:
        At the beginning, the array is [1,2,3,4].
        After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
        After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
        After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
        After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Note:
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    1 <= queries.length <= 10000
    -10000 <= queries[i][0] <= 10000
    0 <= queries[i][1] < A.length
"""

def sumEvenAfterQueries(A, queries):
    # calculate the sum of even nums in list A
    sum = 0
    for num in A:
        if num % 2 == 0:
            sum += num
    # create a list to store the answers
    answers = list()
    # iterate the queries list
    for quire in queries:
        # get the val and index
        val = quire[0]
        index = quire[1]
        # if the original num in position index in list A is even, minus it from sum
        if A[index] % 2 == 0:
            sum -= A[index]
        # add the val to the num in position index in list A
        A[index] += val
        # if the result is even, add it to the sum
        if A[index] % 2 == 0:
            sum += A[index]
        # append the result to the answers list
        answers.append(sum)
    return answers

A1 = [1,2,3,4]
queries1 = [[1,0],[-3,1],[-4,0],[2,3]]

print(sumEvenAfterQueries(A1, queries1))
