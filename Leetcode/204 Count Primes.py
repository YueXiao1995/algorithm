"""
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

# Time Limit Exceeded
"""
def countPrimes(n):
    if n < 2:
        return 0
    num_of_prime = 0
    n = list(range(2, n))
    for num in n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime == True:
            num_of_prime += 1
    return num_of_prime
input1 = 10
"""

def countPrimes(n):
    # if n smaller than 2, return false
    # generate a list which contains the numbers from 2 to n
    n_list = list(range(n))
    # iterate the list n to find and record the prime nums
    num_of_prime = 0

    for i in range(0, n):
        if n_list[i] != -1:
            if i > 1:
                # if the num is a prime, find the nums smaller then n[i] and

                num_of_prime += 1
                index = i + i
                while index < n:
                    n_list[index] = -1
                    index += i

    return num_of_prime
input1 = 10

print(countPrimes(100))
