"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
    Input: name = "leelee", typed = "lleeelee"
    Output: true

Example 4:
    Input: name = "laiden", typed = "laiden"
    Output: true
    Explanation: It's not necessary to long press any character.
"""

def isLongPressedName(name: str, typed: str) -> bool:
    index = 0
    last_char = None
    is_reach_name_end = False
    # iterate over the typed string
    for i in range(len(typed)):
        # check if the char in typed and the char in position index of name are equal
        if typed[i] != name[index]:
            # if not match, check if the char equal to the last visited char in name
            if typed[i] != last_char:
                # if not match, the typed is invalid, return False
                return False
        else:
            # update the last_char
            last_char = name[index]
            # check if the index have reached the end of the name string
            if index < len(name) - 1:
                # update the index of the next char in name string
                index += 1
            else:
                is_reach_name_end = True
    # if reached the end of the name string and have not found any invalid, return True
    if is_reach_name_end:
        return True
    else:
        return False


name1 = "alex"
typed1 = "aaleex"

name2 = "saeed"
typed2 = "ssaaedd"

name3 = "leelee"
typed3 = "lleeelee"

name4 = "laiden"
typed4 = "laiden"

name5 = "vtkgn"
typed5 = "vttkgnn"

name6 = "pyplrz"
typed6 = "ppyypllr"
print(isLongPressedName(name6, typed6))
