"""
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:
    Input: n = 987
    Output: "987"

Example 2:
    Input: n = 1234
    Output: "1.234"

Example 3:
    Input: n = 123456789
    Output: "123.456.789"

Example 4:
    Input: n = 0
    Output: "0"

Constraints:
    0 <= n < 2^31
"""

def thousandSeparator(n):
    n = list(str(n))
    i = len(n) - 3
    while i > 0:
        n.insert(i, ".")
        i -= 3
    return ("").join(n)

n = 987
print(thousandSeparator(n))

n = 1234
print(thousandSeparator(n))

n = 123456789
print(thousandSeparator(n))

n = 0
print(thousandSeparator(n))
