"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
    Input: root = [2,3,1,3,1,null,1]
    Output: 2
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
    Input: root = [9]
    Output: 1

Constraints:
    The given binary tree will have between 1 and 10^5 nodes.
    Node values are digits from 1 to 9.
"""

from binarytree import build
def pseudoPalindromicPaths(root):
    def is_psudo_palindromic_path(permutation):
        digit_freq = dict()
        for digit in permutation:
            if digit not in digit_freq:
                digit_freq[digit] = 1
            else:
                digit_freq[digit] += 1

        freq_list = list(digit_freq.values())
        odd_freq_count = 0
        for i in range(len(freq_list)):
            if freq_list[i] % 2 != 0:
                odd_freq_count += 1
        if odd_freq_count > 1:
            return False
        else:
            return True

    def dfs(root, permutation):
        palindromic_path_count = 0
        if not root.left and not root.right:
            if is_psudo_palindromic_path(permutation + [root.value]):
                return 1
            else:
                return 0
        if root.left:
            palindromic_path_count += dfs(root.left, permutation + [root.value])
        if root.right:
            palindromic_path_count += dfs(root.right, permutation + [root.value])

        return palindromic_path_count

    return dfs(root, [])

root = build([2,3,1,3,1,None,1])
print(pseudoPalindromicPaths(root))
root = build([2,1,1,1,3,None, None, None, None, None,1])
print(pseudoPalindromicPaths(root))
root = build([9])
print(pseudoPalindromicPaths(root))
