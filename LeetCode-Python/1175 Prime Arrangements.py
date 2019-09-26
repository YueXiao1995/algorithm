"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
    Input: n = 5
    Output: 12
    Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:
    Input: n = 100
    Output: 682289015

Constraints:
    1 <= n <= 100
"""
import math
def numPrimeArrangements(n):
    # use a list to store the state of the positions, which represent if a num is not a prime
    position_state = [True] * n
    # iterate over the num from 2 to n (include n)
    num_of_prime = 0
    for i in range(2, n + 1):
        # check the state of the n, if it is not a prime
        if position_state[i - 1] == True:
            # change the state of the positions which can exactly divide the n
            num = i
            while num <= n:
                position_state[num - 1] = False
                num += i
            num_of_prime += 1
    # calculate the num of permutations
    num_of_permutations = math.factorial(num_of_prime) * math.factorial(n - num_of_prime)
    # return the result modulo 10 ^ 9 + 7
    return num_of_permutations % (10 ** 9 + 7)

n1 = 5
n2 = 100
n3 = 1
print(numPrimeArrangements(n3))
