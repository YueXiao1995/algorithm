"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:
    Input: root = [1,null,2,null,3,null,4,null,null]
    Output: [2,1,3,null,null,null,4]
    Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

Constraints:
    The number of nodes in the tree is between 1 and 10^4.
    The tree nodes will have distinct values between 1 and 10^5.
"""

from binarytree import build
def balanceBST(root):

    def balance(root):
        if root.left:
            if root.left.right:
                a = root.left
                b = root.left.right
                c = root
                t1 = root.left.left
                t2 = root.left.right.left
                t3 = root.left.right.right
                t4 = root.right
                a.right = t2
                b.left = a

                c.left = t3
                b.right = c

                return b
            else:
                a = root.left.left
                b = root.left
                c = root
                t1 = root.left.left.left
                t2 = root.left.left.right
                t3 = root.left.right
                t4 = root.right

                b.left = a
                b.right = c
                c.left = t3
                return b
        else:
            if root.right.left:
                a = root
                b = root.right.left
                c = root.right
                t1 = root.left
                t2 = root.right.left.left
                t3 = root.right.left.right
                t4 = root.right.right
                c.left = t3
                b.right = c
                a.right = t2
                b.left = a
                return b
            else:
                a = root
                b = root.right
                c = root.right.right

                t1 = root.left
                t2 = root.right.left
                t3 = root.right.right.left
                t4 = root.right.right.right

                a.right = t2
                b.left = a
                c.left = t3
                b.right = c

                return b

    def dfs(root):
        if not root.left and not root.right:
            return root, 1
        elif root.left and not root.right:
            root.left, left_h = dfs(root.left)

            if left_h > 1:
                root = balance(root)
            return root, 2
        elif not root.left and root.right:
            root.right, right_h = dfs(root.right)

            if right_h > 1:
                print(root)
                root = balance(root)
                print(root)

            return root, 2
        else:
            root.left, left_h = dfs(root.left)
            root.right, right_h = dfs(root.right)

            if abs(left_h - right_h) > 1:
                root = balance(root)
                return root, max(left_h, right_h)
            else:
                return root, max(left_h, right_h) + 1


    root, _ = dfs(root)


    return root

root = build([1,
        None,2,
        None, None, None,3,
        None, None, None, None, None, None, None,4])
print(root)
print(balanceBST(root))
