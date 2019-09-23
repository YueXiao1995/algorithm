"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
    Input: 2
    Output: [0,1,3,2]
    Explanation:
    00 - 0
    01 - 1
    11 - 3
    10 - 2

    For a given n, a gray code sequence may not be uniquely defined.
    For example, [0,2,3,1] is also a valid gray code sequence.

    00 - 0
    10 - 2
    11 - 3
    01 - 1


Example 2:
    Input: 0
    Output: [0]
    Explanation: We define the gray code sequence to begin with 0.
                 A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
                 Therefore, for n = 0 the gray code sequence is [0].
"""

def grayCode(n):
    graycode = list()
    last_code = [0] * n
    graycode.append(last_code)
    l = 1
    for i in range(n):
        l *= 2
    for i in range(1, l):
        newcode = list(last_code)
        if i % 2 != 0:
            if newcode[-1] == 1:
                newcode[-1] = 0
            else:
                newcode[-1] = 1
        else:
            for j in reversed(range(n)):
                if newcode[j] == 1:
                    if newcode[j - 1] == 1:
                        newcode[j - 1] = 0
                    else:
                        newcode[j - 1] = 1
                    break
        graycode.append(newcode)
        last_code = newcode
    result = list()
    for code in graycode:
        newcode = 0
        value = 1
        for i in reversed(range(0, len(code))):
            newcode += int(code[i]) * value
            value *= 2
        result.append(newcode)
    return result


print(grayCode(2))


# more details see https://openhome.cc/Gossip/AlgorithmGossip/GrayCode.htm
