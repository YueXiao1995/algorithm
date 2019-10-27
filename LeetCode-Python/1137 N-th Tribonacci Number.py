"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
    Input: n = 4
    Output: 4
    Explanation:
    T_3 = 0 + 1 + 1 = 2
    T_4 = 1 + 1 + 2 = 4

Example 2:
    Input: n = 25
    Output: 1389537

Constraints:
    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

def tribonacci(n):
    # merge three dict
    def merge(d1, d2, d3):
        new_d = dict()
        for num in d1:
            new_d[num] = d1[num] + d2[num] + d3[num]
        return new_d
    # init
    t = {0: {0: 1, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 0}, 2: {0: 0, 1: 0, 2: 1}}
    # generate t[n]
    for n in range(3, n + 1):
        t[n] = merge(t[n-3], t[n-2], t[n-1])
        del t[n - 3]

    return t[n][1] + t[n][2]

print(tribonacci(25))
