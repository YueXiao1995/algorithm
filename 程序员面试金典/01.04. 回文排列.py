"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

示例1：
    输入："tactcoa"
    输出：true（排列有"tacocat"、"atcocta"，等等）
"""

def canPermutePalindrome(s):
    unique_char = set()
    for char in s:
        if char in unique_char:
            unique_char.remove(char)
        else:
            unique_char.add(char)
    if len(unique_char) <= 1:
        return True
    else:
        return False

# 位运算解法
def canPermutePalindrome2(s):
    mark = 0
    for char in s:
        move = ord(char) - ord(' ')
        if mark & (1 << move) != 0:
            mark ^= (1 << move)
        else:
            mark |= (1 << move)
    count = bin(mark).count('1')
    if count > 1:
        return False
    else:
        return True

s = "tactcoa"
print(canPermutePalindrome2(s))

s = 'aab'
print(canPermutePalindrome2(s))
