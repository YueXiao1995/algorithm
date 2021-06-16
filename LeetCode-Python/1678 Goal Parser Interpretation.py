"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
    Input: command = "G()(al)"
    Output: "Goal"
    Explanation: The Goal Parser interprets the command as follows:
    G -> G
    () -> o
    (al) -> al
    The final concatenated result is "Goal".

Example 2:
    Input: command = "G()()()()(al)"
    Output: "Gooooal"

Example 3:
    Input: command = "(al)G(al)()()G"
    Output: "alGalooG"

Constraints:
    1 <= command.length <= 100
    command consists of "G", "()", and/or "(al)" in some order.
"""


def interpret(command):
    """
    :type command: str
    :rtype: str
    """
    l = len(command)
    i = 0
    s_list = list(command)
    interpretation = list()
    while i < l:
        if s_list[i] == 'G':
            interpretation.append('G')
            i += 1
        elif s_list[i] == '(':
            if s_list[i + 1] == ')':
                interpretation.append('o')
                i += 2
            else:
                interpretation.append('al')
                i += 4
    return ('').join(interpretation)



command = "G()(al)"
print(interpret(command))

command = "G()()()()(al)"
print(interpret(command))

command = "(al)G(al)()()G"
print(interpret(command))
