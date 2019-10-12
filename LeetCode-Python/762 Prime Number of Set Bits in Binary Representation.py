"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:
    Input: L = 6, R = 10
    Output: 4
    Explanation:
    6 -> 110 (2 set bits, 2 is prime)
    7 -> 111 (3 set bits, 3 is prime)
    9 -> 1001 (2 set bits , 2 is prime)
    10->1010 (2 set bits , 2 is prime)

Example 2:
    Input: L = 10, R = 15
    Output: 5
    Explanation:
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)

Note:
    L, R will be integers L <= R in the range [1, 10^6].
    R - L will be at most 10000.
"""

def countPrimeSetBits(L, R):
    result = 0
    for i in range(L, R + 1):
        # convert the num to a binary string and count the number of "1"
        num_of_set_bits = list(str(bin(i))[2:]).count("1")
        # check if the number is a prime
        if num_of_set_bits > 1:
            is_prime = True
            # check if the num of the seb bits has other factor beside 1 and itself
            for j in range(2, num_of_set_bits):
                if num_of_set_bits % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result += 1
    return result


L1 = 6
R1 = 10

L2 = 10
R2 = 15

print(countPrimeSetBits(L2, R2))
