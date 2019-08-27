import math
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
"""


"""
steps：

1: 1 1 1 1 1 
2: 1 1 1 2
3: 1 1 2 1 
4: 1 2 1 1 
5: 2 1 1 1 
6: 2 2 1
7: 2 1 2
8: 1 2 2


"""

def climbStairs(n):
    if n < 3:
        return n
    else:
        result = 0
        max_big_stride = int(n/2)
        for i in range(0, max_big_stride + 1):
            r = i
            k = n - i
            fact_r = 1
            for j in range(1, r + 1):
                fact_r = fact_r * j
            fact_k = 1
            for j in range(1, k + 1):
                fact_k = fact_k * j
            m = k - r
            fact_m = 1
            for j in range(1, m + 1):
                fact_m = fact_m * j
            result += fact_k / (fact_r * fact_m)
            #result += math.factorial(k) / (math.factorial(r) * math.factorial(k-r))
        return int(result)

input = 5
print(climbStairs(input))
