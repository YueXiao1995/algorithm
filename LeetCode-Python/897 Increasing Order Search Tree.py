"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
Note:
    The number of nodes in the given tree will be between 1 and 100.
    Each node will have a unique integer value from 0 to 1000.

"""
from binarytree import build, Node
def increasingBST(root):
    # get all of the values in a increasing order
    def inorder_traversal(root):
        nodes = list()
        if root.left:
            nodes += inorder_traversal(root.left)
        nodes += [root.value]
        if root.right:
            nodes += inorder_traversal(root.right)
        return nodes
    # generate a new tree
    if not root:
        return None
    else:
        increased_list = inorder_traversal(root)
        root = None
        last = None
        for value in increased_list:
            if root == None:
                root = Node(value)
                last = root
            else:
                last.right = Node(value)
                last = last.right
        return root

root1 = build([5,3,6,2,4,None,8,1, None, None,None,None,None,7,9])
print(root1)
print(increasingBST(root1))

