from binarytree import build



def has_path_sum(root, sum:int) -> bool:
    if not root.left and not root.right:
        if root.value == sum:
            return True
        else:
            return False
    sum -= root.value
    is_found = False
    if root.left:
        is_found = has_path_sum(root.left, sum)
    if is_found:
        return True

    if root.right:
        is_found = has_path_sum(root.right, sum)
    if is_found:
        return True

    return is_found


tree = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
print(tree)
print(has_path_sum(tree, 18))


def is_target_in_matrix(matrix, target):
    w = len(matrix[0])
    h = len(matrix)

    for i in range(h):
        for j in range(w):
            print(matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                w = j
                break

    return False
maxtrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22]
          ]
print(is_target_in_matrix(maxtrix, 3))
