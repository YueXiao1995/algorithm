"""
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.

Example 1:
    Input: n = 2
    Output: ["1/2"]
    Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

Example 2:
    Input: n = 3
    Output: ["1/2","1/3","2/3"]

Example 3:
    Input: n = 4
    Output: ["1/2","1/3","1/4","2/3","3/4"]
    Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".

Example 4:
    Input: n = 1
    Output: []

Constraints:
    1 <= n <= 100
"""
import math
def simplifiedFractions(n):
    def getFactors(a):
        factors = set()
        for i in range(2, math.ceil(math.sqrt(a)) + 1):
            if a % i == 0 and i != a:
                factors.add(i)
                factors.add(a//i)
        return list(factors)

    fractions = list()
    for i in range(2, n + 1):
        factors = getFactors(i)
        for j in range(1, i):
            is_simplified = True
            for factor in factors:
                if j >= factor and j % factor == 0:
                    is_simplified = False
                    break
            if is_simplified:
                fractions.append(str(j) + '/' + str(i))
    return fractions


n = 2
print(simplifiedFractions(n))
n = 3
print(simplifiedFractions(n))
n = 4
print(simplifiedFractions(n))
n = 1
print(simplifiedFractions(n))
n = 8
print(simplifiedFractions(n))

