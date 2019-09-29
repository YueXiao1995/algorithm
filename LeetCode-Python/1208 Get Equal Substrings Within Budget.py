"""
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:
    Input: s = "abcd", t = "bcdf", cost = 3
    Output: 3
    Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

Example 2:
    Input: s = "abcd", t = "cdef", cost = 3
    Output: 1
    Explanation: Each charactor in s costs 2 to change to charactor in t, so the maximum length is 1.

Example 3:
    Input: s = "abcd", t = "acde", cost = 0
    Output: 1
    Explanation: You can't make any change, so the maximum length is 1.


Constraints:
    1 <= s.length, t.length <= 10^5
    0 <= maxCost <= 10^6
    s and t only contain lower case English letters.
"""

# Time Limit Exceeded
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    l = len(s)
    cost_list = list()
    for i in range(l):
        cost_list.append(abs(ord(s[i]) - ord(t[i])))
    max_length = 0
    for i in range(l):
        cost = 0
        length = 0
        index = i
        while index < l:
            if cost <= maxCost:
                cost += cost_list[index]
                length += 1
                index += 1
            else:
                break
        if cost > maxCost:
            length -= 1
        if length > max_length:
            max_length = length

    return max_length


s1 = "abcd"
t1 = "bcdf"
cost1 = 3
s2 = "abcd"
t2 = "cdef"
cost2 = 3

s3 = "abcd"
t3 = "acde"
cost3 = 0

s4 = "krrgw"
t4 = "zjxss"
cost4 = 19

s5 = "krpgjbjjznpzdfy"
t5 = "nxargkbydxmsgby"
cost5 = 14
print(equalSubstring(s5, t5, cost5))
