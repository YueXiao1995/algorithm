"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1

    Return 3. The paths that sum to 8 are:

    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11
"""
from binarytree import build
def pathSum(root, sum):

    def find_path(root, sum, path_list):
        valid_path_count = 0

        if not root.left and not root.right:
            for path in path_list:
                if path - root.value == 0:
                    valid_path_count += 1
            return valid_path_count

        new_path_list = list()
        for diff in path_list:
            new_diff = diff - root.value
            new_path_list.append(new_diff)
            if new_diff == 0:
                valid_path_count += 1
        path_list = new_path_list + [sum]

        if root.left:
            valid_path_count += find_path(root.left, sum, path_list)
        if root.right:
            valid_path_count += find_path(root.right, sum, path_list)

        return valid_path_count

    if root == None:
        return 0
    return find_path(root, sum, [sum])

root1 = build([10,5,-3,3,2,None,11,3,-2,None,1])
sum1 = 8
print(root1)
print(pathSum(root1, sum1))

root2 = build([0, 1, 1])
sum2 = 1
print(root2)
print(pathSum(root2, sum2))
