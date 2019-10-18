"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

We should return its max depth, which is 3.

Note:
    The depth of the tree is at most 1000.
    The total number of nodes is at most 5000.
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def maxDepth(root):
    if not root:
        return 0
    max_depth = 0
    for child in root.children:
        depth = maxDepth(child)
        if depth > max_depth:
            max_depth = depth
    return max_depth + 1
