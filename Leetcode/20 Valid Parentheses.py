"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.


Example 1:
    Input: "()"
    Output: true

Example 2:
    Input: "()[]{}"
    Output: true

Example 3:
    Input: "(]"
    Output: false

Example 4:
    Input: "([)]"
    Output: false

Example 5:
    Input: "{[]}"
    Output: true
"""


def isValid(s):
    l = len(s)
    if l == 0:
        return True
    if l%2 != 0:
        return False
    else:
        isValid = True
        # find all of the aixs
        aixs = 0
        index = 0
        bound = 0
        is_aixs_changed = False
        while(index - bound < (l-bound)/2):
            print(index)
            if s[index] == '(':
                if s[index+1] == ')':
                    aixs = index
                    is_aixs_changed = True
                    for j in range(0, aixs-bound +1):
                        if s[index-j] == '(':
                            if s[index+1+j] != ')':
                                return  False
                        elif s[index-j] == '{':
                            if s[index+1+j] != '}':
                                return False
                        elif s[index-j] == '[':
                            if s[index+1+j] != ']':
                                return False
                    index = (aixs + 1) * 2
                    bound = index
                else:
                    index += 1
            elif s[index] == '[':
                if s[index+1] == ']':
                    aixs = index
                    is_aixs_changed = True
                    for j in range(0, aixs-bound +1):
                        print(j)
                        if s[index-j] == '(':
                            if s[index+1+j] != ')':
                                return  False
                        elif s[index-j] == '{':
                            if s[index+1+j] != '}':
                                return False
                        elif s[index-j] == '[':
                            if s[index+1+j] != ']':
                                return False
                    index = (aixs + 1) * 2
                    bound = index
                else:
                    index += 1
            elif s[index] == '{':
                if s[index + 1] == '}':
                    aixs = index
                    is_aixs_changed = True
                    for j in range(0, aixs-bound +1):
                        if s[index - j] == '(':
                            if s[index + 1 + j] != ')':
                                return False
                        elif s[index - j] == '{':
                            if s[index + 1 + j] != '}':
                                return False
                        elif s[index - j] == '[':
                            if s[index + 1 + j] != ']':
                                return False
                    index = (aixs + 1) * 2
                    bound = index
                else:
                    index += 1
            else:
                return False
        if is_aixs_changed != False:
            return isValid
        else:
            return False


input = "()[]{}"
print(isValid(input))

