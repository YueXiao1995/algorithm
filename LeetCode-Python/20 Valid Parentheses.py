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

"""
def isValid(s):
    # store the string into a list
    s = list(s)
    # get the length of the list
    l = len(s)
    # set to True to begin the loop
    is_Valid_found = True
    # if didn't find any valid pairs like '()' or '[]' or '{}', end the loop
    while is_Valid_found:
        # set to False, if do find, change it to True
        is_Valid_found = False
        # find the '()' or '[]' or '{}', and delete them
        i = 0
        while i < l - 1:
            isValid = False
            if (s[i] == '(' and s[i+1] == ')') or (s[i] == '{' and s[i + 1] == '}') or (s[i] == '[' and s[i + 1] == ']'):
                isValid = True
            if isValid:
                is_Valid_found = True
                # delete them from s, and decrease the l by 2, and break the loop
                del s[i]
                del s[i]
                l -= 2
                break
            else:
                i += 1 # increase the index by one

    # check the s is empty now, the original string is valid
    if len(s) == 0:
        return True
    else:
        return False
"""

# This method is ten time faster. When finding the valid, instead of iterating from the first to the last element,
# this method find a first valid pair and delete them, then step back 1 position to find the valid pairs
def isValid(s):
    # store the string into a list
    s = list(s)
    # get the length of the list
    l = len(s)
    # set to True to begin the loop
    is_Valid_found = True
    # if didn't find any valid pairs like '()' or '[]' or '{}', end the loop
    while is_Valid_found:
        # set to False, if do find, change it to True
        is_Valid_found = False
        # find the '()' or '[]' or '{}', and delete them
        i = 0
        while i < l - 1:
            isValid = False
            if (s[i] == '(' and s[i+1] == ')') or (s[i] == '{' and s[i + 1] == '}') or (s[i] == '[' and s[i + 1] == ']'):
                isValid = True
            if isValid:
                is_Valid_found = True
                # delete them from s, and decrease the l by 2, and break the loop
                del s[i]
                del s[i]
                l -= 2
                i -= 1
            else:
                i += 1 # increase the index by one

    # check the s is empty now, the original string is valid
    if len(s) == 0:
        return True
    else:
        return False

# use the stack data structure
def isValid2(s):
    stack = list()
    for char in s:
        if len(stack) > 0:
            if (char == ')' and stack[-1] == '(') or (char == '}' and stack[-1] == '{') or (char == ']' and stack[-1] == '['):
                del stack[-1]
            else:
                stack += [char]
        else:
            stack += [char]
    if len(stack) == 0:
        return True
    else:
        return False

input1 = "()"
input2 = "()[]{}"
input3 = "(]"
input4 = "([)]"
input5 = "{[]}"
input6 = "{[()][][()]}"
print(isValid2(input6))

