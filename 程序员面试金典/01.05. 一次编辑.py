"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:
    输入:
    first = "pale"
    second = "ple"
    输出: True
 
示例 2:
    输入:
    first = "pales"
    second = "pal"
    输出: False
"""

def oneEditAway(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    if len(first) == len(second):
        for i in range(len(second) - 1):
            if first[i] != second[i]:
                if first[i + 1:] != second[i+1:]:
                    return False
                else:
                    return True
        return True

    elif len(first) > len(second):
        for i in range(len(second)):
            if first[i] != second[i]:
                if first[i+1:] != second[i:]:
                    return False
                else:
                    return True
        return True
    else:
        for i in range(len(first)):
            if second[i] != first[i]:
                if second[i + 1:] != first[i:]:
                    return False
                else:
                    return True
        return True


def oneEditAway2(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    for i in range(min(len(first), len(second))):
        if first[i] != second[i]:
            if len(first) > len(second):
                if first[i + 1:] != second[i:]:
                    return False
                else:
                    return True
            elif len(first) == len(second):
                if first[i + 1:] != second[i + 1:]:
                    return False
                else:
                    return True
            else:
                if first[i:] != second[i + 1:]:
                    return False
                else:
                    return True
    return True
first = "pale"
second = "ple"
print(oneEditAway2(first, second))

first = "pales"
second = "pal"
print(oneEditAway(first, second))

first = "intention"
second = "execution"
print(oneEditAway(first, second))
