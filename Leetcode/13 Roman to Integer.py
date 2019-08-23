"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


Roman numerals are usually written largest to smallest from left to right.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

"""

def romanToInt(S):
    roman = list(S)
    result = 0
    l = len(roman)
    i = 0
    while(i < l):
        if roman[i] == 'I':
            if l - i >= 2:
                if roman[i + 1] == "V":
                    result += 4
                    i += 2
                elif roman[i + 1] == "X":
                    result += 9
                    i += 2
                else:
                    result += 1
                    i += 1
            else:
                result += 1
                i += 1
        elif roman[i] == 'X':
            if l - i >= 2:
                if roman[i + 1] == "L":
                    result += 40
                    i += 2
                elif roman[i + 1] == "C":
                    result += 90
                    i += 2
                else:
                    result += 10
                    i += 1
            else:
                result += 10
                i += 1

        elif roman[i] == 'C':
            if l - i >= 2:
                if roman[i + 1] == "D":
                    result += 400
                    i += 2
                elif roman[i + 1] == "M":
                    result += 900
                    i += 2
                else:
                    result += 100
                    i += 1
            else:
                result += 100
                i += 1
        elif roman[i] == 'V':
            result += 5
            i += 1
        elif roman[i] == 'L':
            result += 50
            i += 1
        elif roman[i] == 'D':
            result += 500
            i += 1
        elif roman[i] == 'M':
            result += 1000
            i += 1
    return result
print(romanToInt("DCXXI"))
