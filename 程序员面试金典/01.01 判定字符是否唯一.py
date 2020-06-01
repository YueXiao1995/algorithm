"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：
    输入: s = "leetcode"
    输出: false

示例 2：
    输入: s = "abc"
    输出: true

限制：
    0 <= len(s) <= 100
    如果你不使用额外的数据结构，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 依次判断每个字符是否出现过
def isUnique(astr):
    unique_char = set()
    for char in astr:
        if char in unique_char:
            return False
        else:
            unique_char.add(char)
    return True

# 通过比较set 与 原始list 大小
def isUnique2(astr):
    if len(astr) != len(set(astr)):
        return False
    else:
        return True

# 不使用额外数据结构 双循环 时间复杂度 O(n^2)
def isUnique3(astr):
    for i in range(len(astr)):
        if i >= 1:
            for j in range(i):
                if astr[j] == astr[i]:
                    return False
        if i <= len(astr) - 2:
            for j in range(i + 1, len(astr)):
                if astr[j] == astr[i]:
                    return False
    return True

# 不使用额外数据结构 位运算
def isUnique4(astr):
    mark = 0
    for char in astr:
        move = ord(char) - ord('a')
        if mark & (1 << move) == 0:
            mark |= (1 << move)
        else:
            return False
    return True

s = "leetcode"
print(isUnique4(s))

s = "abc"
print(isUnique4(s))
