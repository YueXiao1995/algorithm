"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.


Example 1:
    Input: tree = [7,4,3,null,null,6,19], target = 3
    Output: 3
    Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Example 2:
    Input: tree = [7], target =  7
    Output: 7

Example 3:
    Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
    Output: 4

Example 4:
    Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
    Output: 5

Example 5:
    Input: tree = [1,2,null,3], target = 2
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [1, 10^4].
    The values of the nodes of the tree are unique.
    target node is a node from the original tree and is not null.
"""
from binarytree import build, Node
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
"""
def getTargetCopy(original, cloned, target):
    def dfsPath(node, target):
        if target == node.value:
            return []
        else:
            if not node.left:
                if not node.right:
                    return None
                else:
                    path = dfsPath(node.right, target)
                    if path != None:
                        return [1] + path
                    else:
                        return None
            else:
                if not node.right:
                    path = dfsPath(node.left, target)
                    if path != None:
                        return [0] + path
                    else:
                        return None
                else:
                    path1 = dfsPath(node.left, target)
                    if path1 != None:
                        return [0] + path1
                    else:
                        path2 = dfsPath(node.right, target)
                        if path2 != None:
                            return [1] + path2
                        else:
                            return None
    target_node_path = dfsPath(original, target)
    print(target_node_path)

    node = cloned
    for path in target_node_path:
        if path == 0:
            node = node.left
        else:
            node = node.right
    return node

tree1 = build([7,4,3,None, None,6,19])
tree2 = build([7,4,3,None, None,6,19])
target = 3
print(getTargetCopy(tree1, tree2, target))

tree1 = build([7])
tree2 = build([7])
target = 7
print(getTargetCopy(tree1, tree2, target))

tree1 = build([1,2,3,4,5,6,7,8,9,10])
tree2 = build([1,2,3,4,5,6,7,8,9,10])
target = 5
print(getTargetCopy(tree1, tree2, target))

tree1 = build([1, 2, None, 3])
tree2 = build([1, 2, None, 3])
target = 2
print(getTargetCopy(tree1, tree2, target))
"""


def getTargetCopy(self, original, cloned, target):
    def findTarget(node, target):
        if target.val == node.val:
            return node
        else:
            if not node.left:
                if not node.right:
                    return None
                else:
                    return findTarget(node.right, target)
            else:
                if not node.right:
                    return findTarget(node.left, target)
                else:
                    left = findTarget(node.left, target)
                    if left != None:
                        return left
                    else:
                        return findTarget(node.right, target)

    return findTarget(cloned, target)
