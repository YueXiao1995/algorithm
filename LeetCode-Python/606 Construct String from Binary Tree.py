"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

from binarytree import build, Node
def tree2str(t):
    if t == None:
        return ""
    char_list = list()
    char_list.append(str(t.value))
    if t.left:
        char_list += ["("] + list(tree2str(t.left)) + [")"]
        if t.right:
            char_list += ["("] + list(tree2str(t.right)) + [")"]
    else:
        if t.right:
            char_list += ["(", ")"] + ["("] + list(tree2str(t.right)) + [")"]
    return ("").join(char_list)

root1 = build([1, 2, 3, 4])
root2 = build([1, 2, 3, None, 4])
print(root1)
print(root2)

print(tree2str(root1))
print(tree2str(root2))
