"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:
    Input: "(()())(())"
    Output: "()()()"
    Explanation:
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
    Input: "(()())(())(()(()))"
    Output: "()()()()(())"
    Explanation:
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:
    Input: "()()"
    Output: ""
    Explanation:
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".

Note:
    S.length <= 10000
    S[i] is "(" or ")"
    S is a valid parentheses string
"""
def removeOuterParentheses(S):
    # use a list to store the index of the outermost parentheses
    index_of_outermost = list()
    # use a stack to store the index,
    index_stack = list()
    # use a stack to store the char
    stack = list()
    # iterate over the chars in S
    for i in range(len(S)):
        # check if there are more than one char in stack
        if len(stack) > 0:
            # check if the last char in stack should be popped
            if S[i] == ")" and stack[-1] == "(":
                # record the outermost parentheses
                if len(stack) == 1:
                    index_of_outermost.append(index_stack[-1])
                    index_of_outermost.append(i)
                # pop the last char in stack
                del stack[-1]
                del index_stack[-1]
            else:
                # push the char into stack
                stack.append(S[i])
                index_stack.append(i)
        else:
            # push the char into stack
            stack.append(S[i])
            index_stack.append(i)
    # remove the outermost parentheses from the S string
    S = list(S)
    for index in reversed(index_of_outermost):
        del S[index]
    return ("").join(S)

input1 = "(()())(())"
input2 = "(()())(())(()(()))"
input3 = "()()"


print(removeOuterParentheses(input3))

