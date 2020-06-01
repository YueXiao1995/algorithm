"""
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

示例1:
     输入："Mr John Smith    ", 13
     输出："Mr%20John%20Smith"

示例2:
     输入："               ", 5
     输出："%20%20%20%20%20"

提示：
    字符串长度在[0, 500000]范围内。
"""

def replaceSpaces(S, length):
    S = list(S)
    for i in range(length):
        if S[i] == " ":
            S[i] = "%20"
    return ('').join(S[:length])

# 超时
def replaceSpaces2(S, length):
    i = 0
    while length > 0:
        if S[i] == " ":
            S = S[0:i] + "%20" + S[i+1:-2]
            i += 2
        i += 1
        length -= 1
    return S[:i]

def replaceSpaces3(S, length):
    URL = list()
    i = 0
    while i < length:
        if S[i] != ' ':
            URL.append(S[i])
        else:
            URL.append('%20')
        i += 1
    return ('').join(URL)



S = "Mr John Smith    "
length = 13
print(replaceSpaces3(S, length))

S = "               "
length = 5
print(replaceSpaces3(S, length))

S = "ds sdfs afs sdfa dfssf asdf             "
length = 27
print(replaceSpaces3(S, length))
