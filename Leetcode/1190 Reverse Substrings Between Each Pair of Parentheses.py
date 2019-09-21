"""
Given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

Example 1:
    Input: s = "(abcd)"
    Output: "dcba"

Example 2:
    Input: s = "(u(love)i)"
    Output: "iloveu"

Example 3:
    Input: s = "(ed(et(oc))el)"
    Output: "leetcode"

Example 4:
    Input: s = "a(bcdefghijkl(mno)p)q"
    Output: "apmnolkjihgfedcbq"

Constraints:
    0 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It's guaranteed that all parentheses are balanced.
"""

def reverseParentheses(s):
    brackets = list()
    bracket_indexs = list()
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == ')':
            brackets.append(s[i])
            bracket_indexs.append(i)

    l = len(brackets)
    while l > 0:
        last = None
        for i in range(0, l):
            if last !=  None:
                if last == "(" and brackets[i] == ")":
                    start = bracket_indexs[i-1] + 1
                    end = bracket_indexs[i]

                    new_string = s[start:end]
                    s_list = new_string[::-1]
                    s = s[:start] + s_list + s[end:]

                    del brackets[i]
                    del brackets[i - 1]
                    del bracket_indexs[i]
                    del bracket_indexs[i - 1]
                    l -= 2
                    break
            last = brackets[i]

    s = list(s)
    l_s = len(s)
    index = 0
    while index < l_s:
        if s[index] == '(' or s[index] ==')':
            del s[index]
            l_s -= 1
        else:
            index += 1
    return "".join(s)

s1 = "(abcd)"
s2 = "(u(love)i)"
s3 = "(ed(et(oc))el)"
s4 = "a(bcdefghijkl(mno)p)q"
s5 = "yfgnxf"
s6 = "ta()usw((((a))))"
print(reverseParentheses(s4))
