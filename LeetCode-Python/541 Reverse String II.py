"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the
start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater
than or equal to k characters, then reverse the first k characters and left the other as original.


Example:
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

Restrictions:
    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
"""


def reverseStr(s, k):
    s = list(s)
    l = len(s)
    index = 0
    while index < l:
        remain = l - index
        if remain < k:
            for i in range(0, remain // 2):
                temp = s[index + i]
                s[index + i] = s[-i-1]
                s[-i-1] = temp
            # reverse all of them
            break
        elif remain >= k and remain < 2 * k:
            for i in range(0, k // 2):
                temp = s[index + i]
                s[index + i] = s[index + k - 1 - i]
                s[index + k - 1 - i] = temp
            # reverse the first k characters
            break
        else:
            # reverse the first k characters
            for i in range(0, k // 2):
                temp = s[index + i]
                s[index + i] = s[index + k - 1 - i]
                s[index + k - 1 - i] = temp
            index += 2 * k
    return ''.join(s)


s = "abcdefg"
s2 = 'abcd'
k = 2
k2 = 4
print(reverseStr(s2, k2))

